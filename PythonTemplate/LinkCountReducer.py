#!/usr/bin/env python3
import sys

current_page = None
current_count = 0
pages = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    page,count = line.split('\t',1)
    count = int(count)
    if page == current_page:
        current_count = current_count + count
    else:
        if current_page:
            pages.append([current_count,current_page])
        current_count = count
        current_page = page

if page == current_page:
    pages.append([current_count,current_page])

pages.sort()

for page in pages:
    print('%s\t%s' % (page[1],page[0]))
# TODO
# print('%s\t%s' % (  ,  )) print as final output
