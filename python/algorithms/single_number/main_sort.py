#!/usr/bin/env python3

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        j = 1
        size = len(nums)
        while (j < size):
            if nums[i] != nums[j]:
                return (nums[i])
            i+=2
            j+=2
        return nums[i]
