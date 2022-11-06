#!/usr/bin/env python3

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        i = 0
        middle = size // 2
        while (i < middle):
            s[i], s[size -1 -i] = s[size -1 -i], s[i]
            i+=1