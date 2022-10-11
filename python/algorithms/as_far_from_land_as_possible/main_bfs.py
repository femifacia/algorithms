#!/usr/bin/env python3

from collections import deque
import math


class Solution:

    def maxDistance(self, grid: list[list[int]]) -> int:
        self.height = len(grid)
        self.width = len(grid[0])
        to_see = deque()
        for i in range(self.height):
            for j in range(self.width):
                if (grid[i][j] == 1):
                    grid[i][j] = -1
                    to_see.appendleft((i,j))
        if (not to_see):
            return -1
        while (to_see):
            i1, j1 = to_see.pop()
            for i2,j2 in [(i1 + 1, j1),(i1 - 1, j1),(i1, j1 + 1),(i1, j1 - 1)]:
                if 0 <= i2 < self.height and 0 <= j2 < self.width and grid[i2][j2] == 0:
                    grid[i2][j2] = grid[i1][j1] + 1 if grid[i1][j1] > 0 else 1
                    to_see.appendleft((i2,j2))
        return (grid[i1][j1])

grid = [[1,0,1],[0,0,0],[1,0,1]]
grid = [[1,0,0],[0,0,0],[0,0,0]]
grid = [[0,0,0],[0,0,0],[0,0,0]]
grid = [[1,0,1],[0,0,0],[1,0,1]]

sol = Solution()
#grid = [[1,0,1],[0,0,0],[1,0,1]]
#grid = [[1,0,0],[0,0,0],[0,0,0]]

print(sol.maxDistance(grid))