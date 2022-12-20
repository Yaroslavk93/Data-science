def search_docs(docs):
    num = input('Введите номер документа: ')
    for i in range(len(docs)):
        if num in docs[i].values():
            print('Владелец документа: %s' % docs[i]['name'])
            break
    else:
        print('Документ не найден в базе.')