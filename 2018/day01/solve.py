#!/usr/bin/env python3

import sys

def get_freq(fp):
    with open(fp, "r") as f:
        return [int(x.strip()) for x in f.readlines()]


def main(argv):
    sum = 0
    for x in get_freq("input"):
        sum += x
    print(sum)


if __name__ == "__main__":
    sys.exit(main(sys.argv))