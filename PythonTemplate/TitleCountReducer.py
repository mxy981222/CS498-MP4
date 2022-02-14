#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
current_word = None
current_count = 0
word = None
countList = []

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)
    if current_word == word:
        current_count = current_count+count
    else:
        if current_word:
            countList.append([current_word,current_count])
        current_count = count
        current_word = word


# TODO
if word == current_word:
    countList.append([current_word,current_count])
countList=sorted(countList, key=itemgetter(1))
countList.reverse()
for element in countList:
    print("%s\t%s" %(element[0],element[1]))
