#!/usr/bin/env python

from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)
        size = len(count)
#        print(count, "ook")
        while size:
            tmp = []
            for i in count:
                tmp.append(i)
                count[i] -= 1
            for i in tmp:
                if count[i] == 0:
                    count.pop(i)
            res.append(tmp)
            #print(count)
            size = len(count)
            
    #        input()
        return res
    
sol = Solution()
nums =  [1,3,4,1,2,3,1]
print(sol.findMatrix(nums)) 