from data import directories


def output(key):
    for i in key:
        print(f'{i}', end=', ')
    print()


def supplement():
    num = input('Введите номер полки: ')
    global directories
    if num not in directories.keys():
        directories[num] = list()
        print('Полка добавлена. Текущий перечень полок: ', end='')
        output(directories.keys())
    else:
        print(f'Такая полка уже существует. Текущий перечень полок: ', end='')
        output(directories.keys())
