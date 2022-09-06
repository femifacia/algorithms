#!/usr/bin/env python3

import sys

class Solution:
    def getSumPos(self, a: int, b: int) -> int:
        while (a!= 0 and b != 0):
#            print("ba", b, "a", a)
            andd = a & b
            a = (a ^ b)
            b = (andd << 1)
#            print("b", b, "a", a)
        if (a):
            return (a)
        return (b)
    def getSumNeg(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (b != 0 and a):
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask
        if a > mask // 2:
            return ~(a ^ mask)
#        print("sheesh", a)
        if (a):
            return (a)
        if b > mask // 2:
            return ~(b ^ mask)
        return b
    def getSum(self, a: int, b: int) -> int:
        if (a < 0 or b < 0):
            return (self.getSumNeg(a, b))
        return (self.getSumPos(a, b))

sol = Solution()
print(sol.getSum(int(sys.argv[1]), int(sys.argv[2])))