#!/usr/bin/env python3

from collections import deque
import math

#don't pass big map

class Solution:

    def bfs(self, grid : list[list[int]], i : int, j : int) -> int:
        dist = -1
        to_see = deque([(i,j)])
        seen = []
        while (to_see):
            i1, j1 = to_see.pop()
            if (i1, j1) in seen:
                continue
            seen.append((i1,j1))
            for i2,j2 in [(i1 + 1, j1),(i1 - 1, j1),(i1, j1 + 1),(i1, j1 - 1)]:
                if 0 <= i2 < self.height and 0 <= j2 < self.width and (i2,j2) not in seen:
                    if grid[i2][j2] == 0:
                        to_see.appendleft((i2,j2))
                    else:
                        return (abs(i2 - i) + abs(j2 - j))
        return -1

    def maxDistance(self, grid: list[list[int]]) -> int:
        dist = -1
        self.height = len(grid)
        self.width = len(grid[0])
        for i in range(self.height):
            for j in range(self.width):
                print(i,j)
                if (grid[i][j] == 0):
                    dist = max(dist,self.bfs(grid, i, j))
        return (dist)

grid = [[1,0,1],[0,0,0],[1,0,1]]
grid = [[1,0,0],[0,0,0],[0,0,0]]
grid = [[0,0,0],[0,0,0],[0,0,0]]
grid = [[1,0,1],[0,0,0],[1,0,1]]

#grid = [[1,0,1],[0,0,0],[1,0,1]]
#grid = [[1,0,1],[0,0,0],[1,0,1]]

sol = Solution()
print(sol.maxDistance(grid))