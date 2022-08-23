#!/usr/bin/env python3
import sys


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = 0
        size1 = len(a) - 1
        size2 = len(b) - 1
        for i in range(len(a)):
            res += int(a[i]) * (2 ** size1)
            size1-=1
        for i in range(len(b)):
            res += int(b[i]) * (2 ** size2)
            size2-=1 
        return (bin(res)[2:])

sol = Solution()

print(sol.addBinary(sys.argv[1], sys.argv[2]))