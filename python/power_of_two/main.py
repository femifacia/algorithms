#!/usr/bin/env python3

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        while (2**i<n):
            i+=1
        return (2**i==n)

sol = Solution()
print(sol.isPowerOfThree(243))