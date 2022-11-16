#!/usr/bin/env python3

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        #this is a decision tree using backtracking
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        backtrack(1, [])
        return res

sol = Solution()
print(sol.combine(4, 3))