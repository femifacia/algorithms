#!/usr/bin/env python

class Solution:
    def minOperations(self, s: str) -> int:
        one = 0
        ref = 0
        for i in s:
            if ord(i) - 48 != ref:
                one += 1
            ref ^= 1
        return min(one, len(s) - one)