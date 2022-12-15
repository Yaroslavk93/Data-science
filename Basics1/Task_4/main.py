width = int(input('Введите ширину: '))
length = int(input('Введите лину: '))
height = int(input('Введите высоту: '))
size = max(width, length, height)

if size <= 15:
    print('Коробка №1')
elif size > 200:
    print('Упаковка для лыж')
elif 50 > size > 15:
    print('Коробка №2')
else:
    print('Коробка №3')