#!/usr/bin/env python3

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        size = len(nums) - 1
        i = 0
        while i < size:
            if nums[i] == nums[i + 1]:
                return (True)
            i += 1
        return (False)