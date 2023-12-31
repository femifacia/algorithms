#!/usr/bin/env python

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        ans = -1
        count = 0

        for i in s:
            if not i in seen:
                seen[i] = count
            else:
                ans = max(ans, count - seen[i] - 1)
            count += 1
            
#        print(seen)
        return ans