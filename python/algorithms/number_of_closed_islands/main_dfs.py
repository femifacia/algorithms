#!/usr/bin/env python3

class Solution:

    def dfs(self, grid : list[list[int]], i : int, j : int) -> None:
        #I replace all grouped 0 by 2 sequence
        grid[i][j] = 2
        for i1, j1 in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if not (0 <= i1 < self.height) or not(0 <= j1 < self.width):
                self.ret = 0
                continue
            if grid[i1][j1] == 0 :
                self.dfs(grid, i1 , j1)

    def closedIsland(self, grid: list[list[int]]) -> int:
        closed_island = 0
        self.height = len(grid)
        self.width = len(grid[0])
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == 0:
                    #when I found a 0 value I init a ret value to 1
                    #then a start a dfs from that (i,j)
                    #if the one 0 of the group starting from (i,j) is connected to an edge, I put the
                    #value of ret to 0.
                    #so if no 0 of the group is connected to an edge, ret is still equal to 1
                    #so the number of closed island is incremented by one
                    self.ret = 1
                    self.dfs(grid, i, j)
                    closed_island += self.ret
        return closed_island

sol = Solution()
grid = [[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
[print(i) for i in grid]
print(sol.closedIsland(grid))
[print(i) for i in grid]
