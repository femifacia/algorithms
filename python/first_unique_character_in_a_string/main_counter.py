#!/usr/bin/env python3

import sys
from typing import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return (-1)


sol = Solution()
print(sol.firstUniqChar(sys.argv[1]))