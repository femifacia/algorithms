#!/usr/bin/env python

from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp = Counter(nums)
        
        ans = 0
        for t in mp.values():
            if t == 1:
                return -1
            ans += t // 3
            if t % 3:
                count += 1
                
        return ans