# Материалы урока

'''import os
from task_HRF import human_read_format

def get_files_sizes():
    for el in os.listdir('data'):
        path = os.path.join('data', el)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            print(path, human_read_format(size))
            size = os.stat(path)
            print(path, human_read_format(size.st_size))

get_files_sizes()'''

import json

json_str = '''{"required_pretests": [], "required_tests": [1], "outcome": 1, "points": 0}'''

data = json.loads(json_str)
print(type(data), data['required_tests'][0])

with open('scoring.json', 'r', encoding='utf=8') as f:
    data = json.load(f)
print(data)

json_str = json.dumps(data)
print(type(json_str), repr(json_str))

with open('copy_scoring.json', 'w', encoding='utf=8') as c_f:
    json.dump(data, c_f, indent=4, ensure_ascii=False)