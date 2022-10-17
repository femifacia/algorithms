#!/usr/bin/env python3

from collections import deque


class Solution:

    def dfs(self, grid : list[list[int]], i : int, j : int, to_see : deque) -> None:
        grid[i][j] = 2
        to_see.appendleft((i, j, 0))
        for i1, j1 in [(i + 1, j), (i, j + 1), (i -1 ,j), (i, j- 1)]:
            if 0 <= i1 < self.height and 0 <= j1 < self.width and grid[i1][j1] == 1:
                self.dfs(grid, i1, j1, to_see)

    def shortestBridge(self, grid: list[list[int]]) -> int:
        self.width = len(grid[0])
        self.height = len(grid)
        to_see = deque()
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, to_see)
                    break
            if (to_see):
                break
        while (to_see):
            i, j, dist = to_see.pop()
            for i1, j1 in [(i + 1, j), (i, j + 1), (i -1 ,j), (i, j- 1)]:
                if 0 <= i1 < self.height and 0 <= j1 < self.width and grid[i1][j1] != 2:
                    if grid[i1][j1] == 1:
                        return dist
                    grid[i1][j1] = 2
                    to_see.appendleft((i1,j1, dist + 1))

sol = Solution()
grid = [[0,1],[1,0]]
grid = [[0,1,0],[0,0,0],[0,0,1]]
grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

print(sol.shortestBridge(grid))
