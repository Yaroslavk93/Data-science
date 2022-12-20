from data import documents, directories
from Task_3.info import info

def ad_doc():
    num_doc = input('Введите номер документа: ')
    type_doc = input('Введите тип документа: ')
    owner = input('Введите владельца документа: ')
    rack = input('Введите полку для хранения: ')
    global documents, directories
    if rack in directories:
        directories[rack].append(num_doc)
        documents.append({'type': type_doc,
                          'number': num_doc,
                          'name': owner})
        print('Документ добавлен. Текущий список документов:')
        info(documents, directories)
    else:
        print('Такой полки не существует. Добавьте полку командой as.\n '
              'Текущий список документов:')
        info(documents,directories)
