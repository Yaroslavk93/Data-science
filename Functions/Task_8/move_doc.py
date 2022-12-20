from data import documents, directories
from Task_3.info import info
from Task_4.supplement import output


def move_doc():
    num_doc = input('Введите номер документа: ')
    num_rack = input('Введите номер полки: ')
    global documents, directories
    if num_rack not in directories.keys():
        print('Такой полки не существует. Текущий перечень полок: ')
        output(directories.keys())
    elif num_doc not in [j for i in directories.values() for j in i]:
        print('Документ не найден в базе.\nТекущий список документов:')
        info(documents, directories)
    else:
        for key, value in directories.items():
            if num_doc in value:
                re_doc = directories[key].pop(directories[key].index(num_doc))
                directories[num_rack].append(re_doc)
        print('Документ перемещен.\nТекущий список документов:')
        info(documents, directories)
    # a = directories['1'].pop(directories['1'].index('11-2'))