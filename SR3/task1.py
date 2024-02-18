import csv
import json

with open('files/subjects.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

    data = []
    for row in reader:
        if row['starting'] != row['ending']:
            print(row)
            data.append({'subject': row['subject'], 'starting': int(row['starting']), 'ending': int(row['ending'])})

with open('files/changes.json', 'w') as js_file:
    json.dump(data, js_file, indent=2)