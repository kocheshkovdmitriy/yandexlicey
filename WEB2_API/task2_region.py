import requests


for obj in ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']:

    url = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b" \
            f"&geocode={obj}&format=json"

    responce = requests.get(url)

    r = responce.json()

    print(obj, ': ',
        r['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']
        ['GeocoderMetaData']['Address']['Components'][1]['name'])
