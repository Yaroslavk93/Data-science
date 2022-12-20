from data import documents, directories
from Task_1.search_docs import search_docs
from Task_2.search_rack import search_rack
from Task_3.info import info
from Task_4.supplement import supplement
from Task_5.delete_rack import delete_rack
from Task_6.ad_doc import ad_doc
from Task_7.del_doc import del_doc
from Task_8.move_doc import move_doc


"""
Функция вызова условий, запрашиваемых команд
Task_1.search_docs (p) - поиск имени владельца по номеру документа
Task_2.search_rack (s)- поиск полки по номеру документа
Task_3.info (l) - вывод информации по всем документам
Task_4.supplement (ads) - добавление новой полки
Task_5.delete_rack (ds) - удаление существующей полки из данных
from Task_6.ad_doc (ad) - добавление нового документа
from Task_7.del_doc (d) - удаление документа из данных
from Task_8.move_doc (m) - перемещение документа с полки на полку
"""


def func(com, docs=documents, direct=directories):
    if com == 'p':
        search_docs(docs)
    elif com == 's':
        search_rack(direct)
    elif com == 'l':
        info(docs, direct)
    elif com == 'ads':
        supplement()
    elif com == 'ds':
        delete_rack()
    elif com == 'ad':
        ad_doc()
    elif com == 'd':
        del_doc()
    elif com == 'm':
        move_doc()
