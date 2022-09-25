#!/usr/bin/env python3
import sys


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        lps = [0] * size
        i = 0
        j = 1
        while (j < size):
            if s[i] != s[j] and i == 0:
                j+=1
            elif s[i] == s[j]:
                lps[j] = i + 1
                i+=1
                j+=1
            else:
                i = lps[i - 1]
        print(lps)
        # we could do this return (size % (size - lps[-1])) == 0 and lps[-1] == max(lps) and lps.count(1)
        return (size % (size - lps[-1])) == 0 and i

sol = Solution()
print(sol.repeatedSubstringPattern(sys.argv[1]))