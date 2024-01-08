#!/usr/bin/env python

from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_seen = set()
        ans = 0
        for i in range(len(mat)):
            count = 0
            tmp = (0,0)
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1
                    tmp = (i,j)
                if count > 1:
                    break
            if count == 1:
                row_seen.add(tmp)
        for y,x in row_seen:
            count = 0
            for i in range(len(mat)):
                if mat[i][x] == 1:
                    count += 1
                if count > 1:
                    break
            if count == 1:
                ans += 1
        return ans