#!/usr/bin/env python3

class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return -1
        if nums[0] > nums[1]:
            mini, maxi = nums[1], nums[0]
        else:
            mini,maxi = nums[0], nums[1]
        i = 2
        if nums[i] > maxi:
            return maxi
        elif nums[i] < mini:
            return mini
        return nums[i]

array = [3,2,1,4]
sol = Solution()
print(sol.findNonMinOrMax(array))