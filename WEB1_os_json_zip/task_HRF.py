# Решение первой класной задачи

def human_read_format(size):
    data = ['', 'К', 'М', 'Г', 'Т']
    for i in range(5):
        if size // 1024 ** i < 1024:
            return f'{round(size / 1024 ** i)}{data[i]}Б'


if __name__ == '__main__':
    for size in [1023, 1024, 2040, 15000, 10 ** 7, 10 ** 10]:
        print(f'{size}: {human_read_format(size)}')