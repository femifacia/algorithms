#!/usr/bin/env python3

import sys

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if (s == p):
            return([0])
        arr = sorted(p)
        res = []
        p = "".join(sorted(arr))
        size = len(s)
        size_word = len(p)
        i = 0
        while (i < size):
            if (not s[i] in arr):
                i+=1
            elif (i + size_word <= size):
                tmp = s[i: i + size_word]
                if ("".join(sorted(tmp)) == p):
                    res.append(i)
                i+=1
            else:
                i+=1
        return res

sol = Solution()

print(sol.findAnagrams(sys.argv[1], sys.argv[2]))