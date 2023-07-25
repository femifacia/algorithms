#!/usr/bin/env python3

class Solution:
    def isFascinating(self, n: int) -> bool:
        left = 2 * n
        right = 3 * n
        n = sorted(str(left) + str(n) + str(right))
        return n == ["1","2","3","4","5","6","7","8","9"]
