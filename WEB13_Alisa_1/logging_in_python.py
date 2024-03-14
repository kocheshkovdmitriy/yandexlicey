import logging

logging.basicConfig(level=logging.INFO,
                    filename='log.txt',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

def summa(n: int):
    temp = 0
    if isinstance(n, str):
        logging.warning('В функцию передали строку вместо числа')
    else:
        for i in range(n + 1):
            logging.debug(i)
            logging.info(i)
            temp += i
    return temp


if __name__ == '__main__':
    print(summa(5))