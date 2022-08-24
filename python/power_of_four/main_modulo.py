#!/usr/bin/env python3

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n!=0 and n % 4==0:
            n/=4
        return n==1

sol = Solution()
print(sol.isPowerOfThree(243))