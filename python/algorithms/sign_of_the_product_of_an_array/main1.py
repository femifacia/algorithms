#!/usr/bin/env python3

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        nums.sort()
        sign = 1
        for i in nums:
            if i == 0:
                return 0
            if i > 0:
                return sign
            sign *= -1
        return sign