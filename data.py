"""
Исходные данные:
documents - перечень документов;
directories - перечень полок, на которых хранятся документы;
com_name - список команд
"""

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

com_name = ('p', 's', 'l', 'ads', 'ds', 'ad', 'd', 'm')
