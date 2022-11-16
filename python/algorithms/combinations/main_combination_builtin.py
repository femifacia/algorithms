#!/usr/bin/env python3

from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = [list(i) for i in combinations(([j for j in range(1, n+1)]), k)]
        return res

sol = Solution()
print(sol.combine(4, 3))