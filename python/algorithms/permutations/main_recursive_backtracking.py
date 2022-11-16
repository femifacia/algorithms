#!/usr/bin/env python3

from itertools import permutations

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backatracking(start, perm, size):
            if size == 0:
                res.append(perm[:])
                return
            for i in nums:
                if i not in start:
                    perm.append(i)
                    backatracking(start + [i], perm, size - 1)
                    perm.pop()
        backatracking([], [], len(nums))
        return res


sol = Solution()

print(sol.permute([1,2,3]))