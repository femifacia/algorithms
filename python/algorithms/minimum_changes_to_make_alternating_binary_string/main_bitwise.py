#!/usr/bin/env python

class Solution:
    def minOperations(self, s: str) -> int:
        one,two=0,0
        ref = 0
        for i in s:
            if i != str(ref):
                one += 1
            else:
                two += 1
            ref ^= 1
        return min(two, one)