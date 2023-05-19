#!/usr/bin/env python3

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums = set(nums)
        full_nums = set(range(len(nums) + 1))
        val = nums & full_nums
        return val.pop()