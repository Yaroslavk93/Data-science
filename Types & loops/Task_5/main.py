import re

car_ids = ['А222ВС96', 'АБ22ВВ193']
my_reg = r'(\w{1}\d{3}\w{2})(\d{2,3})'

for num in car_ids:
    result = re.search(my_reg, num)
    if result:
        print(f'Номер {result.group(1)} '
              f'валиден. Регион: {result.group(2)}')
    else:
        print(f'Номер {num} не валиден')
