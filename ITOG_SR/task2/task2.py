'''
Напишите программу для поиска слабых мест различных миров.

В файле worlds.csv записана информация о мирах (разделители – &) в виде строк:
id, мир, место, слабость
id, world, place, weakness

В файл thin_spot.json запишите словарь слабых мест различных миров, ключ – мир,
значение – список списков [слабость, место], сортировка по списку.

Использование модуля csv обязательно. В примере показано содержимое файлов.
'''

import csv
import json


result = dict()

with open('worlds.csv', 'r', encoding='utf8') as f:
    data = csv.DictReader(f, delimiter='&', quotechar='"')

    for row in data:
        if row['world'] in result.keys():
            result[row['world']].append([row['weakness'], row['place']])
        else:
            result[row['world']] = [[row['weakness'], row['place']]]

for key in result.keys():
    result[key].sort()

with open('thin_spot.json', 'w', encoding='utf8') as f_js:
    json.dump(result, f_js, indent=2)

