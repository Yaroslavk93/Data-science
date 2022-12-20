from data import documents, directories
from Task_3.info import info


def del_doc():
    num_doc = input('Введите номер документа:')
    global documents, directories
    for key_dir, value_dir in directories.items():
        if num_doc in value_dir:
            del directories[key_dir][directories[key_dir].index(num_doc)]
            for i in documents:
                if num_doc in i.values():
                    documents.remove(i)
                    print('Документ удален.\nТекущий список документов:')
                    info(documents, directories)
                    break
            break
    else:
        print('Документ не найден в базе.\nТекущий список документов:')
        info(documents, directories)
