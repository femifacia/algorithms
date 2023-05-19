#!/usr/bin/env python3

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums = set(nums)
        for i in range(len(nums)):
            if not i in nums:
                return i
        return len(nums)