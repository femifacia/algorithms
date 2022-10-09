#!/usr/bin/env python3

class Solution:

    def fill_dfs(self, grid : list[list[int]], i : int, j : int, free : int, to_mark : int) -> None:
        #I replace all grouped 0 by to_mark sequence
        grid[i][j] = to_mark
        for i1, j1 in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if (0 <= i1 < self.height) and (0 <= j1 < self.width) and grid[i1][j1] == free:
                self.fill_dfs(grid, i1, j1, free, to_mark)

    def closedIsland(self, grid: list[list[int]]) -> int:
        closed_island = 0
        self.height = len(grid)
        self.width = len(grid[0])
        #first of all I replace all 0's groups connected to the edge by 1
        #using the two's next for loop
        for i in [0, self.height -1]:
            for j in range(self.width):
                if grid[i][j] == 0:
                    self.fill_dfs(grid, i, j, 0, 1)
        for i in range(1, self.height):
            for j in [0, self.width - 1]:
                if grid[i][j] == 0:
                    self.fill_dfs(grid, i, j, 0, 1)
        #since now all free 0 increment our closed_island and I fill its group with 2
        for i in range(1, self.height):
            for j in range(1, self.width):
                if grid[i][j] == 0:
                    self.fill_dfs(grid, i, j, 0, 2)
                    closed_island += 1
        return closed_island

sol = Solution()
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
grid = [[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]
[print(i) for i in grid]
print(sol.closedIsland(grid))
[print(i) for i in grid]
