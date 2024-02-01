import sys

def main():
    args = sys.argv[1:]
    integers = []
    base = 2
    log = ''
    while args:
        arg = args.pop(0)
        if arg == '--help':
            print('''Скрипт для перевода чисел из произвольной системы счисления в десятичную
                    обязательные ргументы:
                    integers [int...]
                    не обязательные агрументы:
                    --help - помощь
                    --base - система счисления''')
            return
        elif arg == '--base':
            base = int(args.pop(0))
        elif arg == '--log':
            log = args.pop(0)
        elif arg:
            integers.append(arg)
    try:
        integers = list(map(lambda x: int(x, base), integers))
    except ValueError as e:
        print(e)
        return
    if log:
        with open(log, 'w') as f:
            f.write(' '.join(map(str, integers)))
    else:
        print(*integers)


if __name__ == '__main__':
    main()