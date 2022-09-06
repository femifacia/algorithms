#!/usr/bin/env python3

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        while (4**i<n):
            i+=1
        return (4**i==n)

sol = Solution()
print(sol.isPowerOfThree(243))