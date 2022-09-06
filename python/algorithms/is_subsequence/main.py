#!/usr/bin/env python3

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (s == ""):
            return (True)
        idx = 0
        size_s = len(s)
        for i in t:
            if i == s[idx]:
                idx += 1
            if idx == size_s:
                return True
        return False

s1 = "a"
s2 = "aeg"
sol = Solution()
print(sol.isSubsequence(s1, s2))