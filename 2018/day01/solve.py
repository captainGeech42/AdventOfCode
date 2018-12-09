#!/usr/bin/env python3

import sys

def get_freq(fp):
    with open(fp, "r") as f:
        return [int(x.strip()) for x in f.readlines()]


def part1(argv):
    sum = 0
    for x in get_freq("input"):
        sum += x
    print(sum)


def part2(argv):
    sums = []
    sum = 0
    repeat = True
    freqs = get_freq("input")
    while repeat:
        for x in freqs:
            sum += x
            if sum not in sums:
                sums.append(sum)
            else:
                print(sum)
                repeat = False
                break


if __name__ == "__main__":
    # sys.exit(part1(sys.argv))
    sys.exit(part2(sys.argv))