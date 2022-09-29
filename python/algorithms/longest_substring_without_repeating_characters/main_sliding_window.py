#!/usr/bin/env python3

import sys


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        size = len(s)
        j = 0
        longuest = 0
        arr = []
        tmp = 0
        while (j < size):
            if s[j] not in arr:
                tmp +=1
                arr.append(s[j])
                j+=1
                continue
            else:
                #print(s[j:])
                longuest = max(tmp, longuest)
                arr = arr[arr.index(s[j]) + 1:]
                tmp = len(arr)
            print(arr)
        longuest = max(tmp, longuest)
        return longuest

sol = Solution()

print(sol.lengthOfLongestSubstring(sys.argv[1]))
        
