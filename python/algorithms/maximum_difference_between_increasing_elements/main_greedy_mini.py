#!/usr/bin/env python3

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        ans = 0
        mini = nums[0]
        for i in range(1, len(nums) + 1):
            ans = max(ans, nums[i] - mini)
            mini = min(mini, nums[i])
        return ans if ans > 0 else -1