#!/usr/bin/env python3

import sys

def max_interval_intersection(interval):
    B =([(left, +1) for left, right in interval] +
        [(right,-1) for left, right in interval]
    )
    print("B before sort", B)
    B.sort()

    i = 0
    while i  + 1< len(B):
        if (B[i][0] == B[i + 1][0] and B[i][1] < B[i + 1][1]):
            tmp = B[i]
            B[i] = B[i + 1]
            B[i + 1] = tmp
        i+=1
    c = 0
    best = (c, None)
    print("B afterr sort", B)
    for x, d in B:
        c += d
        if best[0] < c:
            best = (c, x)
#            print("new best", best)
    return (best)

if (len(sys.argv) != 2):
    print("Pass the file which countains intervalls as argument", file=sys.__stderr__)
    exit(1)
fd = open(sys.argv[1], 'r')
lines = fd.read().split("\n")
intervals = [i.split(',') for i in lines]
intervals = [[int(i[0]), int(i[1])] for i in intervals]
print("intervals", intervals)
print(max_interval_intersection(intervals))