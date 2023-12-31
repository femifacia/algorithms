#!/usr/bin/env python

from bisect import bisect_left
from bisect import bisect_right
from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        elm_greater = 0
        target_occurences = 0
        for i in nums:
            if i == target:
                target_occurences += 1
            if i > target:
                elm_greater += 1
        left = len(nums) - elm_greater - target_occurences
        right = left + target_occurences
#        print(left, right)
        return [i for i in range(left, right)]