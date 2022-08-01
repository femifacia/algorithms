#!/usr/bin/env python3

import sys 

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            count += ((n >> i) & 1)
        return (count)

numb = int(sys.argv[1])

for i in range(32, -1, -1):
    print((numb >> i) & 1, end="")