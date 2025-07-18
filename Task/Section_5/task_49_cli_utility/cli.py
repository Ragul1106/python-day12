import argparse
from utils import add, sub

parser = argparse.ArgumentParser()
parser.add_argument('x', type=int)
parser.add_argument('y', type=int)
parser.add_argument('--op', choices=['add', 'sub'])

args = parser.parse_args()

if args.op == 'add':
    print("Sum:", add(args.x, args.y))
elif args.op == 'sub':
    print("Diff:", sub(args.x, args.y))