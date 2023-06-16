#!/usr/bin/env python3

class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return -1
        return sorted(nums)[1]