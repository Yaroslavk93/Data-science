import numpy as np


#Task-1
N = int(input('Задание 1\nВведите число: '))
num_ar = np.arange(N - 1, -1, -1)
print(f'{num_ar}\n')

#Task-2
num_d = np.diag(num_ar, k=0)
print(f'Задание 2\n{num_d}\n')

mtx_sum = 0
for i in num_d:
    mtx_sum += sum(i)
print(f'Задание 3\nСумма = {mtx_sum}\n')

#Task-3
a = np.array([
    [4, 2, 1],
    [1, 3, 0],
    [0, 5, 4]
])

b = ([4, 12, -3])

result = np.linalg.solve(a, b)
print(f'Задание 4\n{result}')
print(np.allclose(np.dot(a, result), b))

#Task-5
users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ],
    np.int32
)

next_user_stats = np.array([0, 1, 2, 0, 0, 0])
result = 1000
a = np.array([])
user_id = 0

for user in range(len(users_stats)):
    a_len = np.linalg.norm(users_stats[user])
    b_len = np.linalg.norm(next_user_stats)
    f = np.arccos(np.dot(users_stats[user], next_user_stats) /
                  (a_len * b_len)) * 360 / 2 / np.pi
    if f < result:
        result = f
        a = users_stats[user]
        user_id = user

print(
    f'\nЗадание 4\nУгол м/у векторами {round(result, 2)} градуса(ов)\n'
    f'Пользователь {a}\n'
    f'Номер строки {user_id + 1}'
)

