#!/usr/bin/env python3

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i = 0
        size = len(s)
        ans = 0
        while (i < size):
            ans ^= ord(s[i])
            ans ^= ord(t[i])
            i+=1
        ans ^= ord(t[-1])
        return chr(ans)