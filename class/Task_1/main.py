import requests


def max_curr(url):
    currencies_dict = requests.get(url).json()['Valute']
    result = max(currencies_dict.values(), key=lambda x: x['Value'])
    text = 'Стоимость {name}: {curr}'.format(
        name=result.get('Name'), curr=result.get('Value')
    )
    return text


url_adr = 'https://www.cbr-xml-daily.ru/daily_json.js'
print(max_curr(url_adr))
