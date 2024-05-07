#!/usr/bin/env python

from collections import defaultdict

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = defaultdict(int)
        ans = 0
        # we will count frequency and only get positives one
        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1
        for i in count:
            ans += max(0,count[i])
        return ans