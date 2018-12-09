#!/usr/bin/env python3

import sys

def get_id(fp):
    with open(fp, "r") as f:
        return [x.strip() for x in f.readlines()]


def get_uniq_chr_count(word):
    chrs = {}
    for c in word:
        if c in chrs:
            chrs[c] += 1
        else:
            chrs[c] = 1
    
    two = 2 in chrs.values()
    three = 3 in chrs.values()

    return two, three


def part1(argv):
    two = 0
    three = 0

    for id in get_id("input"):
        two_r, three_r = get_uniq_chr_count(id)
        if two_r:
            two += 1
        if three_r:
            three += 1

    print(two * three)


if __name__ == "__main__":
    sys.exit(part1(sys.argv))