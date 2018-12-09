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


def part2(argv):
    ids = get_id("input")
    good = []
    for x in ids:
        for y in ids:
            if x == y:
                continue
            wrong = False
            broke = False
            for i in range(len(x)):
                if x[i] != y[i] and wrong:
                    broke = True
                    break
                elif x[i] != y[i] and not wrong:
                    wrong = True
            if not broke:
                # we have the two IDs that are only off by one
                good.append(x)
                good.append(y)
                break
        if not broke:
            break
    
    id = ""
    for i in range(len(good[0])):
        if good[0][i] == good[1][i]:
            id += good[0][i]
    
    print(id)


if __name__ == "__main__":
    # sys.exit(part1(sys.argv))
    sys.exit(part2(sys.argv))