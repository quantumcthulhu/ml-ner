import spacy
from spacy.tokens import DocBin
from spacy.training.example import Example
from spacy.training import offsets_to_biluo_tags
from sklearn.model_selection import KFold
import random
import numpy as np
import os
import time
import ast

train_data = []
with open('train_data.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            data = ast.literal_eval(line)
            train_data.append(data)

def check_alignment(text, entities):
    doc = nlp.make_doc(text)
    tags = offsets_to_biluo_tags(doc, entities)
    if '-' in tags:
        print(text)
        print(f"check_alignment(): Misaligned entities in text: {text}")
        for entity in entities:
            start, end, label = entity
            print(f"  - Entity: '{text[start:end]}' with label '{label}' (start: {start}, end: {end})")
        print(f"BILUO Tags: {tags}")
        print("-"*60)
        return False
    return True

n_splits = 5
kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

model_base_dir = "cv_models"
if not os.path.exists(model_base_dir):
    os.makedirs(model_base_dir)

all_f1s = []
all_model_paths = []

for fold_num, (train_index, val_index) in enumerate(kf.split(train_data)):
    print(f"Starting training for fold {fold_num+1}...")
    fold_start_time = time.time()
    
    train_fold = [train_data[i] for i in train_index]
    val_fold = [train_data[i] for i in val_index]
    
    nlp = spacy.blank("en")
    
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")

    for text, annotations in train_fold:
        if check_alignment(text, annotations['entities']):
            for ent in annotations.get('entities'):
                ner.add_label(ent[2])
    
    train_doc_bin = DocBin()
    train_examples = []

    for text, annotations in train_fold:
        if check_alignment(text, annotations['entities']):
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            train_doc_bin.add(example.reference)
            train_examples.append(example)
    
    train_docs = list(train_doc_bin.get_docs(nlp.vocab))
    train_examples = [Example.from_dict(doc, {'entities': doc.ents}) for doc in train_docs]
    
    print(f"Training model for fold {fold_num+1}...")
    train_start_time = time.time()
    optimizer = nlp.begin_training()
    n_iter = 20
    
    for i in range(n_iter):
        random.shuffle(train_examples)
        losses = {}
        for batch in spacy.util.minibatch(train_examples, size=8):
            nlp.update(batch, sgd=optimizer, drop=0.5, losses=losses)
    train_end_time = time.time()
    print(f"Training completed for fold {fold_num+1} in {train_end_time - train_start_time:.2f} seconds.")
    
    print(f"Evaluating model for fold {fold_num+1}...")
    eval_start_time = time.time()
    val_doc_bin = DocBin()
    val_examples = []

    for text, annotations in val_fold:
        if check_alignment(text, annotations['entities']):
            doc = nlp.make_doc(text)
            if annotations['entities']:
                example = Example.from_dict(doc, annotations)
                val_doc_bin.add(doc)
                val_examples.append(example)
            else:
                print(f"Skipping text with no entities: {text}")

    if val_examples:
        scorer = nlp.evaluate(val_examples)
        eval_end_time = time.time()
        print(f"Evaluation completed for fold {fold_num+1} in {eval_end_time - eval_start_time:.2f} seconds.")
        f1_score = scorer['ents_f']
        all_f1s.append(f1_score)
    else:
        print(f"No valid examples for evaluation in fold {fold_num+1}.")
        all_f1s.append(0)

    model_dir = os.path.join(model_base_dir, f"model_fold_{fold_num+1}")
    nlp.to_disk(model_dir)
    all_model_paths.append(model_dir)
    
    fold_end_time = time.time()
    print(f"Fold {fold_num+1} completed in {fold_end_time - fold_start_time:.2f} seconds.")
    print(f"Fold {fold_num+1} - F1: {f1_score if val_examples else 'N/A'}, Model saved to {model_dir}")

best_fold_index = np.argmax(all_f1s)
best_model_path = all_model_paths[best_fold_index]
print(f"Best model is from fold {best_fold_index+1} with F1 score: {all_f1s[best_fold_index]}")

final_model_dir = "best_model"
if os.path.exists(final_model_dir):
    os.system(f"rm -rf {final_model_dir}")
os.system(f"cp -r {best_model_path} {final_model_dir}")

print(f"Best model saved to {final_model_dir}")
