#!/usr/bin/env python
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans = float('-inf')
        nums.sort()
        max_current = nums[0]
        for i in range(1, len(nums)):
            ans = max(ans, (max_current - 1 ) * (nums[i] - 1))
            max_current = max(max_current, nums[i])
        return ans