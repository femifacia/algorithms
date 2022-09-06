#!/usr/bin/env python3

import sys

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        size_p = len(p)
        size_s = len(s)
        if (size_p > size_s):
            return ([])
        if (s == p ):
            return ([0])
        res = []
        left = 0
        right = size_p - 1
        p_count = {}
        s_count = {}
        for i in range(size_p):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
        while (right < size_s):
            if (p_count == s_count):
                res.append(left)
            s_count[s[left]] -= 1
            if (s_count[s[left]] == 0):
                del s_count[s[left]]
            left +=1
            right +=1
            if (right < size_s):
                s_count[s[right]] = 1 + s_count.get(s[right], 0)
        return res

sol = Solution()

print(sol.findAnagrams(sys.argv[1], sys.argv[2]))