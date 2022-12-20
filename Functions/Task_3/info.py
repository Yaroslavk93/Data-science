def info(docs, direct):
    for i in range(len(docs)):
        for key, value in direct.items():
            if docs[i]['number'] in value:
                print(
                    '№: %s, тип: %s, владелец: %s, полка хранения: %s'
                    %(docs[i]['number'], docs[i]['type'],
                      docs[i]['name'], key)
                )
