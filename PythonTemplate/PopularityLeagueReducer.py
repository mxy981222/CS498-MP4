#!/usr/bin/env python3
import sys

league = []
res = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    page,count = line.split("\t",1)
    league.append([int(count),page])

for page in league:
    rank = len([i for i in league if i[0]<page[0]])
    res.append([int(page[1]),rank])

res.sort()
res.reverse()

for page in res:
    print('%s\t%s' % (page[0],page[1]))


#TODO
# print('%s\t%s' % (  ,  )) print as final output
