#!/usr/bin/env python3


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return ( nums[len(nums) // 2])