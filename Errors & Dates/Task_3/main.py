from datetime import datetime, timedelta


def date_range(start_d, end_d, date_list):
    try:
        start_d = datetime.strptime(start_d, '%Y-%m-%d')
        end_d = datetime.strptime(end_d, '%Y-%m-%d')
        while start_d <= end_d:
            date_list.append(start_d.strftime('%Y-%m-%d'))
            start_d += timedelta(days=1)
        return date_list

    except ValueError:
        return date_list


print(date_range('2022-12-15', '2022-12-22', date_list=[]))
print(date_range('2022-155-14', '2022-12-12', date_list=[]))

