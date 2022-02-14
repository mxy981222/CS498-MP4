#!/usr/bin/env python3
import sys

top_pages = []

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    count,word = line.split('\t',1)
    top_pages.append([int(count),word])

top_pages.sort()

for page in top_pages:
    print('%s\t%s' % (page[1],page[0]))
    # print('%s\t%s' % (  ,  )) print as final output
