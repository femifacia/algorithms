#!/usr/bin/env python3

import sys

class Solution:
    def longestPalindrome(self, s: str) -> int:
        nbr = 0
        is_odd = 0
        arr = []
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                arr.append(i)
                dic[i] = 1
        for i in arr:
            if (dic[i] % 2 == 0):
                nbr += dic[i]
            else:
                nbr += (dic[i] - is_odd)
                if (is_odd == 0): 
                    is_odd = 1
        return (nbr)

sol = Solution()
print(sol.longestPalindrome(sys.argv[1]))