#!/usr/bin/env python3

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = 1
        size = len(s)
        while(i < size and s[i] == '1'):
            i+=1
        return not '1' in s[i:]
