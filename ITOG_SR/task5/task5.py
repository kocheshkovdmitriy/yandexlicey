'''
Напишите приложение на flask для получения советов, как преодолеть свой страх.

В файле fear.json записан словарь с ключами:

filename (имя файла базы данных);
fears (типы страхов);
level (нижний уровень страха).
В БД записана таблица советов Advices с полями:
id, fear, advice, level
id, тип страха, совет, снижение уровня страха для данного совета

scheme.png

При обращении по адресу http://127.0.0.1:8080/fear приложение должно возвращать список словарей с ключами:
fear, advice, level
тип страха, совет, уровень

Для типов, записанных в списке, и уровней, не ниже заданного. Список должен быть отсортирован по совету по алфавиту.


Пример
Ввод
# Содержимое файла fear.json
{
   "filename": "fears.db",
   "fears": [
       "height",
       "water",
       "darkness"
   ],
   "level": 5
}


Вывод
[
    {
        "advice": "flashlight",
        "fear": "darkness",
        "level": 8
    },
    {
        "advice": "get used",
        "fear": "darkness",
        "level": 6
    },
    {
        "advice": "go down lower",
        "fear": "height",
        "level": 9
    },
    {
        "advice": "look up",
        "fear": "water",
        "level": 7
    },
    {
        "advice": "suck a lollipop",
        "fear": "water",
        "level": 5
    },
    {
        "advice": "turn on the light",
        "fear": "darkness",
        "level": 5
    }
]

'''