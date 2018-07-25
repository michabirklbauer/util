#!/usr/bin/env python3

# DESCRIPTION
# script to generate random passwords

import random
import sys

def pw_gen(length):

    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alpha = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alpha_u = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    others = ["@", "_", "-", "?", "!"]
    space = num + alpha + alpha_u + others

    pw = ""
    for i in range(length):
        pw = pw + space[random.randint(0, len(space)-1)]

    return pw

if __name__ == '__main__':
    try:
        print(pw_gen(int(sys.argv[1])))
    except IndexError:
        print("Generating password of length 12:")
        print(pw_gen(12))
