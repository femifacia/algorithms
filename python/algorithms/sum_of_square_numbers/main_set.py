#!/usr/bin/env python3

import sys

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        b = round(math.sqrt(c))
        seen = set()
        a = 0
        while a ** 2 + b ** 2 > c:
            b -= 1
        while (1):
            while a ** 2 + b ** 2 < c:
                a += 1
            while a ** 2 + b ** 2 > c and b > 0:
                b -= 1
            if a ** 2 + b ** 2 == c:
                return True
            if a == b:
                return False
            if (a,b) in seen:
                return False
            seen.add((a,b))
        return False

sol = Solution()
print(sol.judgeSquareSum(int(sys.argv[1])))