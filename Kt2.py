import re

def find_emails(text): #Функция
    #Находит все email-адреса в тексте
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' #Регулярные выражения
    return re.findall(pattern, text)

def main(): # главная функция
    try: #Рабоат с ошибками
        # Создаем файл, если его нет
        filename = "data.txt" #Работа с файлами
        
        # Добавляем данные в файл
        with open(filename, 'a', encoding='utf-8') as f: #Функция
            f.write("Моя почта ur1@example.com\n")
            f.write("sudent@mail.ru вдбжваф\n")
            f.write("вдафдфПочта ыджа tes23@gmail.com\n")
            f.write("inov@yandex.ru Почта почта\n")
        
        # Читаем все email из файла
        with open(filename, 'r', encoding='utf-8') as f: #Функция
            emails = []
            for line in f:
                found = find_emails(line)
                emails.extend(found)
        
        # Выводим результаты
        if emails: #Цикл
            print(f"Найдено email: {len(emails)}")
            print("Первые 3 email:")
            for email in emails[:3]:  # Срез первых 3 и цикл
                print(f"  - {email}")
        else: #Цикл
            print("Email не найдены")
            
    except Exception as e: #Работа с ошибками
        print(f"Ошибка: {e}")

# Запуск
main()
