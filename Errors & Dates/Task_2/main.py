from datetime import datetime


def check(dt):
    try:
        datetime.strptime(dt, '%Y-%m-%d')
        return True
    except ValueError:
        return False


stream = ['2018-04-02', '2018-02-29', '2018-19-02']
for i in stream:
    print(check(i))
