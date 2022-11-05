#!/usr/bin/env python3

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        i = len(nums) -1
        nbr = 0
        while (i - 2 >= 0):
            nbr = nums[i - 2] + nums[i - 1] 
            if  nbr > nums[i]:
                return nbr + nums[i]
        return 0