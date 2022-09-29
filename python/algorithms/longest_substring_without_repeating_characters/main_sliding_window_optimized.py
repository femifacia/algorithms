#!/usr/bin/env python3

import sys


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        j = 0
        longuest = 0
        arr = []
        while (j < size):
            if s[j] not in arr:
                arr.append(s[j])
                j+=1
            else:
                longuest = max(len(arr), longuest)
                arr = arr[arr.index(s[j]) + 1:]
        longuest = max(len(arr), longuest)
        return longuest

sol = Solution()

print(sol.lengthOfLongestSubstring(sys.argv[1]))
        
