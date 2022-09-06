#!/usr/bin/env python3

class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1,2,3]
        for i in range(3, n):
            f.append(f[i - 2] + f[i - 1])
        return (f[n- 1])