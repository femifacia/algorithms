#!/usr/bin/env python3
import sys

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]
sol = Solution()

print(sol.addBinary(sys.argv[1], sys.argv[2]))