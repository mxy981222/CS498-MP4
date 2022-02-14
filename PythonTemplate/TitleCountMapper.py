#!/usr/bin/env python3

import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

delimiters = ""
stopWords = []

with open(stopWordsPath) as f:
    stopWord = f.readline()
    while stopWord:
        stopWords.append(stopWord.strip())
        stopWord = f.readline()

f.close()

with open(delimitersPath) as f:
    delimiters = f.read()

f.close()        

for line in sys.stdin:
    line = line.strip()
    words = [line]
    for i in range(0,len(delimiters)):
        delimiter = delimiters[i]
        count = len(words)
        for j in range(0,count):
            word = words[0].split(delimiter)
            words = words + word
            words.pop(0)
    for word in words:
        word = word.lower()
        if word not in stopWords and word != '':
            val = 1
            print('%s\t%s' %(word,val))
