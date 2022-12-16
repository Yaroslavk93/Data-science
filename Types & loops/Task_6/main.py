import re

stream = [
    'user4,2021-01-01;3',
    'user3,2022-01-07;4',
    'user2,2022-03-29;1',
    'user1,2020-04-04;13',
    'user2,2022-01-05;7',
    'user1,2021-06-14;4',
    'user3,2022-07-02;10',
    'user4,2021-03-21;19',
    'user4,2022-03-22;4',
    'user4,2022-04-22;8',
    'user4,2021-05-03;9',
    'user4,2022-05-11;11'
]

my_reg = r'user(\d),\d{4}-\d{2}-\d{2};(\d{1,})'
user_dict = dict()


for user in stream:
    search = re.search(my_reg, user)
    if search.group(1) not in user_dict:
        user_dict[search.group(1)] = [int(search.group(2))]
    else:
        user_dict[search.group(1)].append(int(search.group(2)))

for key, value in user_dict.items():
    user_dict[key] = sum(value)

print(f'Среднее количество просмотров на уникального пользователя: '
      f'{sum(user_dict.values()) / len(user_dict.keys())}')

