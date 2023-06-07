#!/usr/bin/env python3

import sys

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        i = 0
        ans = 0
        limit = max(a,b,c)
        while 1<<i <= limit:
            if c & (1 << i) == 0:
                if a & (1 << i) and b & (1 << i):
                    ans += 2
                elif a & (1 << i) or b & (1 << i):
                    ans += 1
            else:
                if a & (1 << i) or b & (1 << i):
                    i+=1
                    continue
                ans += 1
            i+=1
        return ans


sol = Solution()
print(sol.minFlips(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))