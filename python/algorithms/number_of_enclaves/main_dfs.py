#!/usr/bin/env python3

class Solution:

    def dfs(self, grid : list[list[int]], i : int, j : int) -> None:
        #I replace all grouped 1 by 2 sequence
        grid[i][j] = 2
        #when I find a free land I uncrement my size pointer
        self.size += 1
        for i1, j1 in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if not (0 <= i1 < self.height) or not(0 <= j1 < self.width):
                self.ret = 0
                continue
            if grid[i1][j1] == 1 :
                self.dfs(grid, i1 , j1)

    def numEnclaves(self, grid: list[list[int]]) -> int:
        enclave = 0
        self.height = len(grid)
        self.width = len(grid[0])
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == 1:
                    #when I found a 0 value I init a ret value to 1 and size value to 0
                    #then a start a dfs from that (i,j)
                    #if the  group of 1  from (i,j) is connected to an edge, I put the
                    #value of ret to 0.
                    #so if no 1 in the group is connected to an edge, ret is still equal to 1
                    #so the number of closed island is incremented by size if there is no 
                    #land connected to the boundaries
                    #size is calculated during the dfs phase
                    self.size = 0
                    self.ret = 1
                    self.dfs(grid, i, j)
                    self.size = self.size if self.ret else 0
                    enclave += self.size
        return enclave

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
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
[print(i) for i in grid]
print(sol.numEnclaves(grid))
[print(i) for i in grid]
