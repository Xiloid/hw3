"""
    Программа считает сумму/разницу/произведение/частное n чисел.
    Алгоритм:
    1. Пользователь вводит число n.
    2. Затем выбирает операцию (+, -, *, /).
    3. После этого вводит n чисел.
    4. Программа выводит результат и сообщение "Continue? (y/n)".
    5. Если пользователь вводит y, то программа выполняется сначала.
        Иначе - выводит сообщение 'Bye!' и прекращает свою работу.
"""
answer = "y"
while answer == "y":
    result = 0
    iteration = 0
    oper = None
    print() # отступ первой строки
    n = int(input('Количество итераций: '))
    oper = input('Оператор (+, -, /, *:) ')
    if oper == '/':
        numb = int(input('Введите число: '))
        result = numb
        while iteration != n - 1:
            numb = int(input('Введите число: '))
            if numb != 0:
                result = result / numb
                iteration += 1
            else:
                print('На ноль делить нельзя! Введите снова!')
                continue
        print('Результат:', result)
    elif oper == '-':
        numb = int(input('Enter a number: '))
        result = numb
        while iteration != n - 1:
            numb = int(input('Введите число: '))
            result = result - numb
            iteration += 1
        print('Результат:', result)
    elif oper == '+':
        numb = int(input('Введите число: '))
        result = numb
        while iteration != n - 1:
            numb = int(input('Введите число: '))
            result = result + numb
            iteration += 1
        print('Результат:', result)
    elif oper == '*':
        numb = int(input('Введите число: '))
        result = numb
        while iteration != n - 1:
            numb = int(input('Введите число: '))
            result = result * numb
            iteration += 1
        print('Результат:', result)
    else:
        print('Неправильный оператор!')
    answer = input("Продолжить? y/n ")
    if answer == "n":
        print('Пока!')
