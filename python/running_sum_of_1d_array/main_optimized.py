#!/usr/bin/env python3

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            nums[i + 1] += nums[i]
        return (nums)

sol = Solution()
arr=[1,2,3,4]
print(sol.runningSum(arr))
