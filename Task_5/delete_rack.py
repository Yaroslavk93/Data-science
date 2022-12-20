from data import directories
from Task_4.supplement import output


def delete_rack():
    num = input('Введите номер полки: ')
    global directories
    if num not in directories:
        print('Такой полки не существует. Текущий перечень полок: ', end='')
        output(directories.keys())
    elif (num in directories) and (not directories[num]):
        del directories[num]
        print('Полка удалена. Текущий перечень полок: ', end='')
        output(directories.keys())
    else:
        print('На полке есть документы, удалите их перед удалением полки. '
              'Текущий перечень полок: ', end='')
        output(directories.keys())

