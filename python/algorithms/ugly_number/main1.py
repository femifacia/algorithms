#!/usr/bin/env python3

class Solution:
    def isUgly(self, n: int) -> bool:
        arr = [2,3,5]
        if n <= 0:
            return False
        while n > 1:
            print(n)
            for i in arr:
                if n % i == 0:
                    n = n // i
                    break
            else:
                return False
        return True

sol = Solution()
nbr = -2147483648
print(sol.isUgly(nbr))