#!/usr/bin/env python3

class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return -1
        if nums[0] > nums[1]:
            mini, maxi = nums[1], nums[0]
        else:
            mini,maxi = nums[0], nums[1]
        for i in range(2, len(nums)):
            if nums[i] > maxi:
                return maxi
            elif nums[i] < mini:
                return mini
            else: 
                return nums[i]

array = [3,2,1,4]
sol = Solution()
print(sol.findNonMinOrMax(array))