#!/usr/bin/env python3

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        val = 0
        for i in nums:
            val -= i
        for i in range(len(nums) + 1):
            val += i
        return val
