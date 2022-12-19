stats = {
    'facebook': 55,
    'yandex': 115,
    'vk': 120,
    'google': 99,
    'email': 42,
    'ok': 98
}

# 1 Вариант
for key in stats.keys():
    if stats[key] == max(stats.values()):
        print(f'Максимальный объем продаж на рекламном канале: {key}')

# 2 Вариант
print(
    f'Максимальный объем продаж на рекламном канале: '
    f'{max(stats, key=stats.get)}'
)

