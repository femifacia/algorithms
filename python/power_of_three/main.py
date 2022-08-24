#!/usr/bin/env python3

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        while (3**i<n):
            i+=1
        return (3**i==n)

sol = Solution()
print(sol.isPowerOfThree(243))