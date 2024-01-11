# решение второй классной задачи
import os
from task_HRF import human_read_format

def get_files_sizes():
    for el in os.listdir('data'):
        path = os.path.join('data', el)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            print(path, human_read_format(size))


get_files_sizes()