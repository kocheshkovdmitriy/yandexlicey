import sqlite3

db_name = 'landing.db'

place = 'chalk hills'
danger = 5

con = sqlite3.connect(db_name)
cursor = con.cursor()
r = cursor.execute(f'''
SELECT s.what, s.time, p.name 
FROM Situations as s
INNER JOIN Pixie as p
ON  s.with_whom = p.id
WHERE place = '{place}' and danger >= {danger}
''').fetchall()


import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i, el in enumerate(r):
        spamwriter.writerow([i + 1] + list(el))

