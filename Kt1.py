# Ввести два целых числа a и b (a<=b). 
# Вывести таблицу умножения для чисел [a...b] на [1...10].
# Использовать только while, сделать выравнивание столбцов по ширине (len(str(...))). 

a = int(input('первое число: '))
b = int(input('второе число: '))

# Находим максимальное значение в таблице умножения для определения ширины столбцов
max_value = b * 10
max_width = len(str(max_value))

num = a
while num <= b:
    multiplier = 1
    while multiplier <= 10:
        result = num * multiplier
        # Формируем строку с выравниванием
        print(f"{num} * {multiplier} = {result:>{max_width}}", end="")
        
        # Добавляем разделители, кроме последнего столбца
        if multiplier < 10:
            print(", ", end="")
        
        multiplier += 1
    print()  # Переход на новую строку для следующего числа
    num += 1