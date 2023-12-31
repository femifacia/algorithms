#!/usr/bin/env python

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        ans = -1
        count = 0

        for i in s:
            seen[i] = seen.get(i, []) + [count]
            count+=1
#        print(seen)
        for i in seen:
#            for j in range(len(seen[i]) - 1):
#                print(i)
            ans = max(ans, seen[i][- 1] -1 -seen[i][0])
        return ans