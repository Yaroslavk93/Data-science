count = 0

while True:
    digit = int(input('Введите число: '))
    if digit != 0:
        count += digit
    else:
        break

print(f'Результат: {count}')