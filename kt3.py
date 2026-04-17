import random
import datetime

# Список возможных ID событий/мест
event_ids = [101, 102, 103, 104, 105]

# Список возможных ID посетителей
visitor_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]

# Статусы посещения
statuses = ["вошёл", "вышел"]

# Количество записей для генерации
num_records = 50

# Создаём список для хранения всех записей
all_records = []

print("Генерация журнала посещений")

# Генерируем записи
for i in range(num_records):
    event_id = random.choice(event_ids)
    visitor_id = random.choice(visitor_ids)
    
    year = 2026
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(8, 20)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    
    event_datetime = datetime.datetime(year, month, day, hour, minute, second)
    status = random.choice(statuses)
    
    # Создаём запись в виде строки (а не словаря)
    record = f"{event_id} | {event_datetime.strftime('%Y-%m-%d %H:%M:%S')} | {visitor_id} | {status}"
    
    all_records.append(record)

# Сортируем записи (сортировка по дате сложнее для строк, но можно)
all_records.sort()

# Сохраняем в обычный текстовый файл
filename = "journal_poseshcheniy.txt"

with open(filename, 'w', encoding='utf-8') as file:
    # Записываем заголовок
    file.write("ID события | Дата и время | ID посетителя | Статус\n")
    
    # Записываем все записи
    for record in all_records:
        file.write(record + "\n")

print(f"Готово! Создан файл: {filename}")
print(f"Всего сгенерировано записей: {len(all_records)}")

# Показываем первые 5 записей
print("\nПример первых 5 записей:")
for i in range(min(5, len(all_records))):
    print(all_records[i])
