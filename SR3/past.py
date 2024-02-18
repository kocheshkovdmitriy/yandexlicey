import io
import logging
from json import dumps
from time import sleep

from flask import Flask
from multiprocessing import Process
from contextlib import contextmanager, redirect_stdout

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = [
        {
            'living_room': [112, 227, 156, 115, 69, 58],
            'library': [289, 198, 127, 56],
            'bath': [259, 143, 142],
            'master_bedroom': [2, 39, 171, 169, 290]
        },
        {
            'yard': [203, 119, 133, 276, 272],
            'office': [268, 104, 1, 189, 176, 161, 123],
            'kitchen': [210, 186, 63, 52],
            'living_room': [95, 49, 187, 10, 3, 270]
        }
    ]

    index = 0
    while (index := int(input('Р’РІРµРґРёС‚Рµ РЅРѕРјРµСЂ РїСЂРёРјРµСЂР°: '))) not in (1, 2):
        ...
    server = Server('127.0.0.1', 5000, data[index - 1])
    with server.run():
        while (row := input('Р’РІРµРґРёС‚Рµ "stop" РґР»СЏ Р·Р°РІРµСЂС€РµРЅРёСЏ СЂР°Р±РѕС‚С‹ СЃРµСЂРІРµСЂР°: ')) != 'stop':
            ...
