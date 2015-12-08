#!/usr/bin/python3

from program import Program
import sys


def main():
    p = Program(sys.argv[1:])
    p.work()


if __name__ == "__main__":
    main()
