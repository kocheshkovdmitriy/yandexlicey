import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-b', metavar='--base', type=int, default=2, help='Система счисления')
parser.add_argument('intedgers',
                    type=str, nargs='+',
                    help='Список целых чисел в системе счисления BASE (по умолчанию 2)')
parser.add_argument('-l', metavar='--log', default=sys.stdout,
                    type=argparse.FileType('w'), help='Имя файла')
args = parser.parse_args()

print(*list(map(lambda x: int(x, args.b), args.intedgers)), file=args.l)
