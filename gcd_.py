"""
    Алгоритм Евклида. НОД - наибольший общий делитель
    1. Большее число делим на меньшее.
    2. Если делится без остатка, то меньшее число и есть НОД (выходим из цикла)
    3. Если есть остаток, то большее число заменяем на остаток от деления.
    4. Переходим к 1 пункту.
"""
first = second = ostatok = nod = None
try:
    first = int(input('Первое число: '))
    second = int(input('Второе число: '))
except ValueError:
    exit("Введено не целое число!")
if (first and second) > 0:
    while ostatok != 0:
        if first > second:
            ostatok = first % second
            if ostatok == 0:
              nod = second
            else:
                first = ostatok
        else:
            ostatok = second % first
            if ostatok == 0:
                nod = first
            else:
                second = ostatok
    print('НОД равен:', nod)
else:
    print('Введено отрицательное число')
