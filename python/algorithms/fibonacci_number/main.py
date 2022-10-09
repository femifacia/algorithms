#!/usr/bin/env python3

import sys


class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        for i in range (2, n + 1):
            f.append(f[i - 1] + f[i - 2])
        return(f[n])

sol = Solution()
print(sol.fib(int(sys.argv[1])))