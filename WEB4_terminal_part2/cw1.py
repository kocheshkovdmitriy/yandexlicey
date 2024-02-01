import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs="*")
args = parser.parse_args()

if args.arg:
    for el in args.arg:
        print(el)
else:
    print("no args")
