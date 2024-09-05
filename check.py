import ast

# Функція для читання даних з train_data.txt
def read_train_data(file_path):
    train_data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Пропуск порожніх рядків
                data = ast.literal_eval(line)
                train_data.append(data)
    return train_data

# Функція для перевірки сутностей
def check_entities(train_data):
    for idx, (text, annotations) in enumerate(train_data):
        print(f"\nExample {idx + 1}:")
        print(f"Text: {text}")
        print("Entities:")
        for entity in annotations.get("entities", []):
            start, end, label = entity
            entity_text = text[start:end]
            print(f"  - {label}: '{entity_text}' (start: {start}, end: {end})")

# Шлях до файлу з даними
file_path = 'train_data.txt'

# Зчитування та перевірка даних
train_data = read_train_data(file_path)
check_entities(train_data)
