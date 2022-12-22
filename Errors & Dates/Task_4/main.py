#1) Ошибка IndexError: list index out of range означает
# попытку обратиться к элементу списка с несуществующим индексом

#2) После первого запуска функции, из списка удаляется последний элемент.
# Т.к сам список находится в качестве аргумента в самой функции,
# он напрямую изменяет своё состояние после вызова.
# После 2 вызова остаётся 1 элемент в списке,
# и мы не можем вернуть предпоследний несуществующий элемент

#3) Как по мне, сам список лучше передавать при вызове функции,
# а не в самой функции.

def delete_and_return_last_user(
        region, default_list=['A100', 'A101', 'A102']
):
    element_to_delete = default_list[-1]
    default_list.remove(element_to_delete)
    return default_list[DEFAULT_USER_COUNT - 2]


DEFAULT_USER_COUNT = 3

delete_and_return_last_user(1)
delete_and_return_last_user(1)

