#!/usr/bin/env python3

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        ans = 0
        maxi = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            ans = max(ans, maxi - nums[i])
            maxi = max(maxi, nums[i])
        return ans if ans > 0 else -1