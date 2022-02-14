#!/usr/bin/env python3
import sys

c = 5
top_pages = []
pages = []

for line in sys.stdin:
    line = line.strip()
    page, count = line.split('\t',1)
    pages.append([page,count])

top_pages = pages[-10:]

for page in top_pages:
    print('%s\t%s' % (page[0],page[1]))



#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
