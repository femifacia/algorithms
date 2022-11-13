#!/usr/bin/env python3

from collections import Counter

import sys

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        size1 = len(s1)
        size2 = len(s2)
        if size1 > size2:
            return False
        count1 = Counter(s1)
        count2 = Counter(s2[0:size1 - 1])
        j = size1 - 1
        while (j < size2):
            count2[s2[j]] = count2.get(s2[j], 0) + 1
            if (count2 == count1):
                return True 
            count2[s2[i]] -= 1
            if (count2[s2[i]] == 0):
                count2.pop(s2[i])
            j+=1
            i+=1
        return False

sol = Solution()
print(sol.checkInclusion(sys.argv[1], sys.argv[2]))