#!/usr/bin/env python3

from itertools import permutations

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = [list(i) for i in permutations(nums)]
        return res

sol = Solution()
print(sol.permute([1,2,3]))