import json


purchases = dict()

with open('purchase_log.txt', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        line = line.strip()
        result = json.loads(line)
        purchases[result['user_id']] = result['category']

print(purchases)

