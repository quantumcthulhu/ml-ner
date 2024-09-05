import re
from datasets import load_dataset

dataset = load_dataset('flowfree/crypto-news-headlines')
train_dataset = dataset['train']
test_dataset = dataset['test']

entities = []
with open('train_entities.txt', 'r') as f:
    for line in f:
        name, category = line.strip().rsplit(' ', 1)
        entities.append((name, category))

def find_entities(text, entities):
    entity_positions = []
    occupied_indices = set()
    
    for entity, category in entities:
        pattern = r'(?<![\w@])' + re.escape(entity) + r'(?!\w)'
        for match in re.finditer(pattern, text):
            start, end = match.start(), match.end()

            if not any(i in occupied_indices for i in range(start, end)):
                entity_positions.append((start, end, category))
                occupied_indices.update(range(start, end))
    
    return entity_positions

train_data = []
for item in train_dataset:
    text = item['text']
    entities_in_text = find_entities(text, entities)
    if entities_in_text:
        train_data.append((text, {"entities": entities_in_text}))

for entry in train_data:
    print(entry)
