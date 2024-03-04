#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(
    prog="Tree",
    description="Print an ASCII art of a simple tree"
)
parser.add_argument("size", metavar="size", type=int, nargs='?')
args = parser.parse_args()


def tree(size=5):
    for i in range(size+1):
        print(" "*(size-i), end="")
        print("* " * i)
    print(" " * (size-1), end="")
    print("#")


def main():
    if args.size:
        tree(args.size)
    else:
        tree()


if __name__ == "__main__":
    main()
