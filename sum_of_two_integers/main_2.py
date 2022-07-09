#!/usr/bin/env python3

import sys

class Solution:
    def getSum(self, a: int, b: int) -> int:
        count = 0
        carry = 0
        res = 0
        for i in range (32):
            b_a =(a >> i) & 1
            b_b = (b >> i) & 1
            res = ((a >> i) & 1) ^ ((b >> i) & 1)
        return (res)

sol = Solution()
print(sol.getSum(int(sys.argv[1]), int(sys.argv[2])))