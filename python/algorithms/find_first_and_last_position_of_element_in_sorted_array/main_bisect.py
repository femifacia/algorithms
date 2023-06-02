#!/usr/bin/env python3

import bisect

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1,-1]
        size = len(nums)
        left = bisect.bisect_left(nums,target)
        if left >= size or nums[left] != target:
            left = -1
        right = left
        while right + 1 < size and nums[right + 1] == target:
            right += 1
        return [left, right]