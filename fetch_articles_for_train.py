from datasets import load_dataset

dataset = load_dataset('flowfree/crypto-news-headlines')

train_dataset = dataset['train']
test_dataset = dataset['test']

with open('train_articles.txt', 'w') as train_file:
    for item in train_dataset:
        train_file.write(item['text'] + '\n')

with open('test_articles.txt', 'w') as test_file:
    for item in test_dataset:
        test_file.write(item['text'] + '\n')
