#!/usr/bin/env python3

import sys


class Solution:

    def adjustResult(self, result, signe):
        if (result < 2147483648):
            return result if signe != 1 else -result
        if (signe != 1):
            return 2147483647
        return -2147483648

    def divide(self, dividend: int, divisor: int) -> int:
        signe = 0
        if (dividend < 0):
            signe += 1
            dividend = - dividend
        if (divisor < 0):
            signe += 1
            divisor = - divisor
        res = 0
        if (divisor == 1):
            return self.adjustResult(dividend, signe)
        while (dividend >= divisor):
            dividend -= divisor
            res += 1
        return self.adjustResult(res, signe)


sol = Solution()
print(sol.divide(int(sys.argv[1]), int(sys.argv[2])))