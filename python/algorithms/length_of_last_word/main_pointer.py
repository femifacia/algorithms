#!/usr/bin/env python3

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        size = 0
        while (index >= 0 and s[index] == " "):
            index -= 1
        while (index >= 0 and s[index] != " "):
            index -= 1
            size +=1
        return size