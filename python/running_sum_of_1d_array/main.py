#!/usr/bin/env python3

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        val = nums[0]
        for i in range(1, len(nums)):
            nums[i] += val
            val = nums[i]
        return (nums)

sol = Solution()
arr=[1,2,3,4]
print(sol.runningSum(arr))
