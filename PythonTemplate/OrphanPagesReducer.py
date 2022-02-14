#!/usr/bin/env python3
import sys

pages = set()
dests = set()

for line in sys.stdin:
    line = line.strip()
    src, dest = line.split('\t',1)
    src = int(src)
    dest = int(dest)
    pages.add(src)
    pages.add(dest)
    dests.add(dest)

orphans = list(pages-dests)
orphans.sort()

for orphan in orphans:
    print(orphan)

#TODO
# print(xx) print as final output
