#!/usr/bin/env python3
import sys
import math

count_max = 0
count_min = sys.maxsize
count_mean = 0
count_sum = 0
count_var = 0
c = 0
counts = []

for line in sys.stdin:
    line = line.strip()
    _, count = line.split('\t',1)
    count = int(count)
    if count < count_min:
        count_min = count
    if count > count_max:
        count_max = count
    count_sum = count_sum + count
    c = c + 1
    counts.append(count)

count_mean = math.floor(count_sum/c)
for count in counts:
    count_var = count_var + math.pow(count-count_mean,2)

count_var = math.floor(count_var / c)

#TODO
print('%s\t%s' % ("Mean",count_mean))
print('%s\t%s' % ("Sum",count_sum))
print('%s\t%s' % ("Min",count_min))
print('%s\t%s' % ("Max",count_max))
print('%s\t%s' % ("Var",count_var))
