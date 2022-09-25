#!/usr/bin/env python3
import sys


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        i = 1
        while (size // i >= 2):
            if (s[0:i] * (size // i) == s):
                return (True)
            i += 1
        return (False)

sol = Solution()
print(sol.repeatedSubstringPattern(sys.argv[1]))