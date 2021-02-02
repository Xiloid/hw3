""" При запуске программы выбор:
    1. Найти количество четных и нечетных цифр числа.
    2. Найти факториал числа.
    3. Вывести последовательность чисел в степени до предела.
    4. Выход.
    * после выполнения пунктов 1-3 попадаем обратно в меню.
"""
flag = 0
number = 0
menu = None
while flag != 1:
    print()
    print('1. Найти количество четных и нечетных цифр числа.')
    print('2. Найти факториал числа.')
    print('3. Вывести последовательность чисел в степени до предела.')
    print('4. Выход.')
    try:
        menu = int(input('Введите пункт меню: '))
    except ValueError:
        exit('Введено НЕ число!')   # Можно было бы обрабатывать эти события при помощи while и возвращаться в меню,
# но такие конструкции, как по мне, сильно перегрузят код.
    if menu == 1:
        even = odd = last_digit = 0
        try:
            number = int(input('Введите число: '))
        except ValueError:
            exit('Введено НЕ число!')
        while number > 0:
            last_digit = number % 10
            if last_digit % 2 == 0:
                even += 1
            else:
                odd += 1
            number //= 10
        print("Четных:", even)
        print("Нечетных:", odd)
    elif menu == 2:
        try:
            number = int(input('Введите число факториала: '))
        except ValueError:
            exit('Введено НЕ число!')
        factorial = 1
        while number > 1:
            factorial *= number
            number -= 1
        print('Факториал числа', number, 'равен:', factorial)
    elif menu == 3:
        p = limit = None
        try:
            p = int(input('Введите степень: '))
            limit = int(input('Введите предел: '))
        except ValueError:
            exit('Введено НЕ число!')
        while (result := number ** p) < limit:
            print(result)
            number += 1
    elif menu == 4:
        flag = 1
        exit('Выход...')
