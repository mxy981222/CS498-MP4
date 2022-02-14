#!/usr/bin/env python3
import sys

pages = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    page,count = line.split('\t',1)
    count = int(count)
    pages.append([count,page])

pages.sort()

for page in pages:
    print("%s\t%s" %(page[1],page[0]))
