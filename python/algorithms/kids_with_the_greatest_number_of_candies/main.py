#!/usr/bin/env python

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = [i + extraCandies >= max_candies for i in candies]
        return res