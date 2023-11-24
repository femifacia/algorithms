#!/usr/bin/env python3


class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ans = max(nums[j] - nums[i], ans)
        return ans if ans > 0 else -1