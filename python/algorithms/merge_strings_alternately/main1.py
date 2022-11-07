#!/usr/bin/env python3

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i = 0
        size1 = len(word1)
        size2  = len(word2)
        while (i < size1 and i < size2):
            ans += word1[i]
            ans += word2[i]
            i+=1
        if i < size1:
            return ans + word1[i:]
        return ans + word2[i:]