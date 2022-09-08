#!/usr/bin/env python3

class Solution:

    def dfsMaxArea(self, grid, i, j):
        grid[i][j] = 5
        for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if (0 <= a < self.height and 0 <= b < self.length and grid[a][b] == 1):
                self.curr += 1
                self.dfsMaxArea(grid, a, b)

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        number = 0
        self.length = len(grid[0])
        self.height = len(grid)
        self.curr = 0
        for i in range(self.height):
            for j in range(self.length):
                if (grid[i][j] == 1):
                    self.curr = 1
                    self.dfsMaxArea(grid, i, j)
                    number = max(number, self.curr)
        return (number)

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
grid  = [[1,1,1,1,1,1],
[1,1,0,0,1,1],
[1,1,0,0,1,1]
]
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
sol = Solution()
print(sol.maxAreaOfIsland(grid))
[print(i) for i in grid]
