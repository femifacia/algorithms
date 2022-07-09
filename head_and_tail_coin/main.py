#!/usr/bin/env python3
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, q = [int(i) for i in input().split()]
head = [i for i in range(n)]
tail = []
coins = [i for i in range(n)]
#head = coins[:]
for i in range(q):
    l, r = [int(j) for j in input().split()]
    for i in range(n):
        if (i <= r and i >= l):
            if coins[i] in head:
                head.remove(coins[i])
                tail.append(coins[i])
            elif coins[i] in tail:
                tail.remove(coins[i])
                head.append(coins[i])
print(len(tail))