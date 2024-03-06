import requests
from pprint import  pprint

print('Получение списка новостей:')
rec = requests.get('http://127.0.0.1:5000/api/v2/news')
print(f'Статус код ответа: {rec.status_code} Ответ: {rec.json()}')



pprint(requests.get('http://127.0.0.1:5000/api/v2/news/11').json())
pprint(requests.get('http://127.0.0.1:5000/api/v2/news/15').json())
print('Get new 12:')
pprint(requests.get('http://127.0.0.1:5000/api/v2/news/12').json())
print('Delete new 12:')
pprint(requests.delete('http://127.0.0.1:5000/api/v2/news/12').json())
print('Get new 12:')
pprint(requests.get('http://127.0.0.1:5000/api/v2/news/12').json())

pprint(requests.put('http://127.0.0.1:5000/api/v2/news/11', json={'title': 'news 11', 'content': 'Текст новости', 'user_id': 1}).json())