while True:
    number = int(input('Введите шестизначное число: '))
    if len(str(number)) != 6:
        print('Ошибка: "Введите естизначное число!"')
    else:
        break

frst_num, snd_num = list(str(number // 1000)), list(str(number % 1000))
f_sum = int(frst_num[0]) + int(frst_num[1]) + int(frst_num[2])
s_sum = int(snd_num[0]) + int(snd_num[1]) + int(snd_num[2])

if f_sum == s_sum:
    print('Счастливый билет')
else:
    print('Несчастливый билет')