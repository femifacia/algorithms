#!/usr/bin/env python3

import sys

class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        size = len(s)
        while i + 1 < size:
            if s[i] == s[i + 1]:
                s = s[0:i] + s[i+2:]
                size -= 2
#                print(s, i)
                i -= 1 if i else 0
                continue
            i+=1
        return s

sol = Solution()
print(sol.removeDuplicates(sys.argv[1]))