#!/usr/bin/env python3

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            if - nums[i] in nums:
                return nums[i]
        return -1