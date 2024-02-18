import requests
import json


with open('dinner.json', 'r') as js_file:
    data = json.load(js_file)

url = f'http://{data["host"]}:{data["port"]}'
response = requests.get(url=url).json()

result = []
for recept in response:
    for key in recept:
        if key != 'receipt':
            if key not in data or recept[key] > data[key]:
                break
    else:
        result.append(recept['receipt'])
print(*sorted(result), sep='\n')
