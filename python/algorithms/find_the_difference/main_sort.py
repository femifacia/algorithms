#!/usr/bin/env python3

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i = 0
        size = len(s)
        s = sorted(s)
        t = sorted(t)
        while (i < size):
            if s[i] != t[i]:
                break
            i+=1
        return t[i]