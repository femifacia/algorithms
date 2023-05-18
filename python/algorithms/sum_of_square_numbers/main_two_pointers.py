#!/usr/bin/env python3

import sys

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        b = round(math.sqrt(c))
        a = 0
        while a ** 2 + b ** 2 > c:
            b -= 1
        while (a <= b):
            while a ** 2 + b ** 2 < c:
                a += 1
            while a ** 2 + b ** 2 > c and b > 0:
                b -= 1
            if a ** 2 + b ** 2 == c:
                return True
        return False

sol = Solution()
print(sol.judgeSquareSum(int(sys.argv[1])))