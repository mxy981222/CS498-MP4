#!/usr/bin/env python3
import sys



# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    count,word = line.split('\t',1)
    print('%s\t%s' % (word,count))
    # print('%s\t%s' % (  ,  )) print as final output
