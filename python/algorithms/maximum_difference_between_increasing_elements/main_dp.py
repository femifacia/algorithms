#!/usr/bin/env python3

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        ans = 0
        dp = [-float('inf')] * len(nums)
        dp[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = max(dp[i+1], nums[i])
        for i in range(len(nums)):
            ans = max(dp[i] - nums[i], ans)
        return ans if ans > 0 else -1