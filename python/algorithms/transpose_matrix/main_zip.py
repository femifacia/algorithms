#!/usr/bin/env python

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in zip(*matrix):
            ans.append(list(i))
        return ans

sol = Solution()
matrix = [
    [0,3,2],
    [1,1,1],
    [9,9,9],
    [1,3,4]
]
[print(i) for i in sol.transpose(matrix)]