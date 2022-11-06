#!/usr/bin/env python3

import sys

class Solution:
    def recursive(self, n : int, maxi : int, seen : dict) -> bool:
#        print(n, maxi)
        if n == 1:
            return True
        if n > maxi or n in seen:
            return False
        seen[n] = 1
        numb = 0
        while (n > 0):
            numb += pow(n % 10,2)
            n //=10
        return self.recursive(numb, maxi, seen)
    
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        seen = {}
        seen[n] = 1
        numb = 0
        i = 0
        while (n > 0):
            numb += pow(n % 10,2)
            n //=10
            i += 1
        return self.recursive(numb, 10 ** (i + 2), seen)

sol = Solution()
print(sol.isHappy(int(sys.argv[1])))