#!/usr/bin/env python3

# DESCRIPTION
# script to download twitter pictures from a linklist

import urllib.request as ur
import sys

def twdl(link_file):
    with open(link_file, "r") as f:
        links = f.readlines()
        f.close()

    for link in links:
        s = link.split("/")[-1].split(":")[0]
        ur.urlretrieve(link, s)

if __name__ == '__main__':
    twdl(sys.argv[1])
