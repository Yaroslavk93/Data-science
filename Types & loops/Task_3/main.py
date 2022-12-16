def test(man, woman):
    if len(man) == len(woman):
        man, woman = sorted(man), sorted(woman)
        print('Идеальные пары:')
        for pair in range(len(man)):
            print(f'{man[pair]} и {woman[pair]}')
    else:
        print('\nВнимание, кто-то может остаться без пары!')


boys_1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls_1 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
test(boys_1, girls_1)

boys_2 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls_2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
test(boys_2, girls_2)
