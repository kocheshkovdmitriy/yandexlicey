# решение второй классной задачи
import os


def get_files_sizes():
    for el in os.listdir():
        path = os.path.join(el)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            print(path, human_read_format(size))


def human_read_format(size):
    data = ['', 'К', 'М', 'Г', 'Т']
    for i in range(5):
        if size // 1024 ** i < 1024:
            return f'{round(size / 1024 ** i)}{data[i]}Б'


get_files_sizes()