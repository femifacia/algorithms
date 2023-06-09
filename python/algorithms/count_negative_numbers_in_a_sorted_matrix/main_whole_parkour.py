#!/usr/bin/env python3

#TC : O(n*m)
#SP : O(1)

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        ans = 0
        for i in grid:
            for j in i:
                if j < 0:
                    ans += 1
        return ans