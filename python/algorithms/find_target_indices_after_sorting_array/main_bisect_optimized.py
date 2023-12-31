#!/usr/bin/env python

from bisect import bisect_left
from bisect import bisect_right
from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        return [i for i in range(left, right)]