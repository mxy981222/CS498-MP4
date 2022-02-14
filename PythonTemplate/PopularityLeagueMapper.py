#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]
league = []
pages = {}


with open(leaguePath) as f:
    tmp = f.readline()
    while tmp:
        league.append(tmp.strip())
        tmp = f.readline()

f.close()

for line in sys.stdin:
    line = line.strip()
    page, count = line.split("\t",1)
    pages[page] = int(count)

for page in league:
    if page in pages:
        print("%s\t%s" %(page,pages[page]))
