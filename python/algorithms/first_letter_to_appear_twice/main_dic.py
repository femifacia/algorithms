#!/usr/bin/env python3

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                return i
            dic[i] = 1