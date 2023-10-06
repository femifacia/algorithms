#!/usr/bin/env python3

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0] * (len(nums))
        for i in range(len(nums)):
            dp[i] = nums[i] + max(0, dp[i-1])
        return max(dp)