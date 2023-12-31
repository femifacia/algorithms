#!/usr/bin/env python

from bisect import bisect_left
from bisect import bisect_right
from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        size = len(nums)
        left = bisect_left(nums, target)
        right = left
        while right < size and nums[right] == target:
            right += 1
        return [i for i in range(left, right)]