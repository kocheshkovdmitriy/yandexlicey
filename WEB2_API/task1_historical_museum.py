import requests

url = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b" \
        f"&geocode=Москва, Красная пл-дь, 1&format=json"

responce = requests.get(url)

r = responce.json()

print("Адрес Исторического музея: ", r['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text'])
print('Координаты: ', r['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'])