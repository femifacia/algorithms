#!/usr/bin/env python3

class Solution:

    def dfs(self, grid1 : list[list[int]], grid2 : list[list[int]], i, j) -> None:
        grid2[i][j] = 2
        if grid1[i][j] != 1:
            self.ret = 0
        for i1, j1 in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if 0 <= i1 < self.height and 0 <= j1 < self.width and grid2[i1][j1] == 1:
                self.dfs(grid1, grid2, i1, j1)

    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        self.width = len(grid1[0])
        self.height = len(grid1)
        sub_island = 0
        for i in range(self.height):
            for j in range(self.width):
                if grid2[i][j] == 1:
                    self.ret = 1
                    self.dfs(grid1, grid2, i, j)
                    sub_island += self.ret
        return (sub_island)

sol = Solution()
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
print(sol.countSubIslands(grid1, grid2))