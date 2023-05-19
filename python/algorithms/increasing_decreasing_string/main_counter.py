#!/usr/bin/env python3
from collections import Counter

import sys

class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        letters = set(s)
        letters_inc = sorted(letters)
        letters_dec = letters_inc[::-1]
        string = ""
        index = 0
        size = len(s)
        while (index < size):
            for i in letters_inc:
                if count[i] > 0:
                    string += i
                    count[i] -= 1
                    index += 1
            for i in letters_dec:
                if count[i] > 0:
                    string += i
                    count[i] -= 1
                    index += 1
        return string

sol = Solution()
string =  sys.argv[1]
print(sol.sortString(string))
