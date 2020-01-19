import argparse

parser = argparse.ArgumentParser(description='Command Line args example')

parser.add_argument('count', action="store", type=int)
parser.add_argument('units', action="store")
parser.add_argument('-a')

print(parser.parse_args())

