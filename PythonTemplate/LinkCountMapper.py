#!/usr/bin/env python3
import sys


for line in sys.stdin:
    line = line.strip()
    src, dests = line.split(":")
    dest_list = dests.split(' ')
    for dest in dest_list:
        if dest != '':
            print('%s\t%s' % (dest,1))    

  # print('%s\t%s' % (  ,  )) pass this output to reducer
