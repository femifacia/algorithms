#!/usr/bin/env python3

import sys

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        i = 0
        ans = 0
        while a > 0 or b > 0 or c > 0:
            if c & 1 == 0:
                if a & 1 and b & 1:
                    ans += 2
                elif a & 1 or b & 1 << i:
                    ans += 1
            else:
                if a & 1 or b & 1 :
                    a >>= 1
                    b >>= 1
                    c >>= 1
                    continue
                ans += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return ans


sol = Solution()
print(sol.minFlips(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))