#!/usr/bin/env python3

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        return sorted(nums)[-3]