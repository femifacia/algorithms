#!/usr/bin/env python3

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return sorted(nums)[-k]