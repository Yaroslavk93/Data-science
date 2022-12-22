from datetime import datetime


newspapers = {
    'The Moscow Times': 'Wednesday, October 2, 2002',
    'The Guardian': 'Friday, 11.10.13',
    'Daily News': 'Thursday, 18 August 1977'
}


newspapers['The Moscow Times'] = datetime.strptime(
    newspapers['The Moscow Times'], '%A, %B %d, %Y'
).date()

newspapers['The Guardian'] = datetime.strptime(
    newspapers['The Guardian'], '%A, %d.%m.%y'
).date()

newspapers['Daily News'] = datetime.strptime(
    newspapers['Daily News'], '%A, %d %B %Y'
).date()

for key, value in newspapers.items():
    print(f'{key} - {value}')