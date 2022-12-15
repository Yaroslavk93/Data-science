while True:
    year = int(input('Введите год: '))
    if 0 <= year <= 9999:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print('Високосный год')
            break
        else:
            print('Обычный год')
            break
    else:
        print('Введите значение от 0 до 9999.\n')