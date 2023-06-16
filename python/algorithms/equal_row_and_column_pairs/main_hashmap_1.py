#!/usr/bin/env python3

from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        col = defaultdict(int)
        row = defaultdict(int)
        for i in grid:
            string = ""
            for j in i:
                string += (str(j) + ',')
            row[string] += 1
        height = len(grid)
        width = len(grid[0])
        i = 0
        while (i < width):
            j = 0
            string = ""
            while(j < height):
                string += (str(grid[j][i]) + ',')
                j+=1
            col[string] += 1
            i+=1
        inter = row.keys() & col.keys()
        ans = 0
        for i in inter:
            ans += (col[i] * row[i])
#        print(row,col)
#        print(inter)
        return ans