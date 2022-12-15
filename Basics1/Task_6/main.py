from math import pi, sqrt

figure_list = ['Круг', 'Треугольник', 'Прямоугольник']

while True:
    figure = input(
        'Введите тип фигуры (Круг, Треугольник, Прямоугольник): '
    ).capitalize()
    if figure not in figure_list:
        print('Введите одно из 3х значений: Круг, Треугольник, Прямоугольник')
    else:
        break


if figure == figure_list[0]:
    r = int(input('\nВведите радиус круга: '))
    S = pi * r**2
    print(f'Площадь круга: {round(S, 2)}')

elif figure == figure_list[1]:
    while True:
        side = input('\nВведите длину стороны A, B, C через пробел: ').split()
        if len(side) != 3:
            print('Ошибка: "Введите 3 стороны через пробел,'
                  ' используя числовые значения"')
        elif side[0].isalpha() \
                or side[1].isalpha() \
                or side[2].isalpha():
            print('Используйте только числовые значения')
        else:
            break
    p = (int(side[0]) + int(side[1]) + int(side[2])) / 2
    S = sqrt(p * (p - int(side[0])) * (p - int(side[1])) * (p - int(side[2])))
    print(f'Площадь треугольника: {round(S, 2)}')

else:
    side_1 = int(input('Введите первую сторону прямоугольника: '))
    side_2 = int(input('Введите вторую сторону прямоугольника: '))
    S = side_1 * side_2
    print(f'Площадь прямоугольника: {S}')