#!/usr/bin/env python

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        i,j = 0,0
        size1 = len(g)
        size2 = len(s)
        while i < size1 and j < size2:
            while i < size1 and j < size2 and g[i] > s[j]:
                j+=1
            if j < size2 and s[j] >= g[i]:
                ans += 1
            i+=1
            j+=1
        return ans