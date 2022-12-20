def search_rack(direct):
    num = input('Введите номер документа: ')
    for key, value in direct.items():
        if num in value:
            print(f'Документ хранится на полке: {key}')
            break
    else:
        print('Документ не найден в базе.')