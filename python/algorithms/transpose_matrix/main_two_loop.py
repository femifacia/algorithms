#!/usr/bin/env python

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        width = len(matrix[0])
        height = len(matrix)

        trans = [[0 for i in range(height)] for i in range(width)]
        y = 0
        x = 0
        for i in matrix:
            for j in i:
                trans[y][x] = j
                y+=1
            y = 0
            x += 1
        return trans