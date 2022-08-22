#!/usr/bin/env python3

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return not(len(nums) == len(list(set(nums))))