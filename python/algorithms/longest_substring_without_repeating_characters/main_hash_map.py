#!/usr/bin/env python3

import sys


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        size = len(s)
        j = 0
        longuest = 0
        dic = {}
        tmp = 0
        while (j < size):
            if s[j] not in dic:
                tmp +=1
                dic[s[j]] = j
                j+=1
                continue
            else:
                #print(s[j:])
                j = dic[s[j]] + 1
                dic = {}
                longuest = max(tmp, longuest)
                tmp = 0
        longuest = max(tmp, longuest)
        return longuest

sol = Solution()

print(sol.lengthOfLongestSubstring(sys.argv[1]))
        
