#!/usr/bin/env python

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        ans = 0
        for i in count_s:
            if i not in count_t:
                ans += count_s[i]
            else:
                ans += abs(count_s[i] - count_t[i])
        #thanks to this loop we count the difference between t and s
        #in s but not in t
        for i in count_t:
            if i not in count_s:
                ans += count_t[i]
        #now our ans would contain all the differences between s and t
        # and t and s. And if you figure about this, this value is doubled
        # because when having for example s="bab" and t="aba", counting
        # difference between s and t wound have b = 1 diff and a = 1 diff
        # because abs(1-2) = 1 for a case.
        #we counted differences twice

        #so we return ans divided by two
        return ans // 2