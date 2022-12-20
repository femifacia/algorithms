#!/usr/bin/env python3

import sys

#not optimized

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            while s[i] == s[j] and i < j:
                j-=1
                i+=1
            if i < j:
                return s[i+1:j+1] == s[i+1:j+1][::-1] or s[i:j] == s[i:j][::-1]
        return True


sol = Solution()
print(sol.validPalindrome(sys.argv[1]))
#for i,j in enumerate(sys.argv[1]):
#    print(i,j)