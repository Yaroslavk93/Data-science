from datetime import datetime


def num_day(num_month, days):
    result = int(datetime(datetime.now().year, num_month, days).strftime('%j'))
    return result


month_dict = {
    'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4,
    'Май': 5, 'Июнь': 6, 'Июль': 7, 'Август': 8,
    'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12
}

zodiac_dict = {
    'Овен': [num_day(3, 21), num_day(4, 20)],
    'Телец': [num_day(4, 21), num_day(5, 21)],
    'Близнецы': [num_day(5, 22), num_day(6, 21)],
    'Рак': [num_day(6, 22), num_day(7, 22)],
    'Лев': [num_day(7, 23), num_day(8, 21)],
    'Дева': [num_day(8, 22), num_day(9, 23)],
    'Весы': [num_day(9, 24), num_day(10, 23)],
    'Скорпион': [num_day(10, 24), num_day(11, 22)],
    'Стрелец': [num_day(11, 23), num_day(12, 22)],
    'Козерог': [num_day(12, 23), num_day(1, 20) + num_day(12, 23)],
    'Водолей': [num_day(1, 21), num_day(2, 19)],
    'Рыбы': [num_day(2, 20), num_day(3, 20)]
}

day = int(input('Введите день: '))
month = input('Введите месяц: ').capitalize()

date = num_day(month_dict[month], day)
if date <= 20:
    date = zodiac_dict['Козерог'][0] + date

for key, value in zodiac_dict.items():
    if value[0] <= date <= value[1]:
        print(f'Ваш знак зодиака: {key}')
        break

