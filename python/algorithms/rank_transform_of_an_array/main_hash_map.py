#!/usr/bin/env python

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_nums = sorted(arr)
        rank = {}
        count = 1
        for i in range(len(sorted_nums)):
            if sorted_nums[i] in rank:
                continue
            rank[sorted_nums[i]] = count
            count += 1
        ans = []
        for i in arr:
            ans.append(rank[i])
        return ans