#!/usr/bin/env python3


import sys

class Solution:
    def isPalindrome(self, s: str) -> bool:
        size = len(s)
        s = s.upper()
        i = j =  0
        while (i + j < size):
            while  (i + j < size and not s[i].isalnum()):
                i+=1
            while  (i + j < size and not s[size -j - 1].isalnum()):
                j+=1
            if (i + j < size and s[i] != s[size-j-1]):
                return (False)
            i+=1
            j+=1
        return (True)

sol = Solution()
print(sol.isPalindrome(sys.argv[1]))