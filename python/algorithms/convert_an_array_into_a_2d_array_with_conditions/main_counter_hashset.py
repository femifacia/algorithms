#!/usr/bin/env python

from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)
        size = len(count)
        while size:
            to_erase = set()
            tmp = []
            for i in count:
                tmp.append(i)
                count[i] -= 1
                if count[i] == 0:
                    to_erase.add(i)
            for i in to_erase:
                count.pop(i)
            res.append(tmp)
            size = len(count)
        return res
    
sol = Solution()
nums =  [1,3,4,1,2,3,1]
print(sol.findMatrix(nums)) 