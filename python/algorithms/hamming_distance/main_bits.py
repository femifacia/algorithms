#!/usr/bin/env python3

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        for i in range(32):
            place =  1 << i
            if (place & x) != (place & y):
                count += 1
        return count
