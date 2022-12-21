import csv
import json

purchases = dict()

with open('purchase_log.txt', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        line = line.strip()
        result = json.loads(line)
        purchases[result['user_id']] = result['category']


with open('visit_log.csv') as visit:
    with open('funnel.csv', 'w', encoding='utf-8') as funnel:
        names = ['user_id', 'source', 'category']
        funnel_writer = csv.DictWriter(
            funnel, delimiter=',', lineterminator="\r", fieldnames=names
        )
        for i in visit:
            res = i.strip().split(',')
            if res[0] in purchases.keys():
                funnel_writer.writerow({
                    'user_id': res[0], 'source': res[1], 'category': purchases[res[0]]
                })
