#!/usr/bin/env python3

class Solution:

    def dfs_mark_island(self, grid :list[list[str]], i, j, to_mark, island_char):
        grid[i][j] = to_mark
        for a, b in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j- 1)]:
            if (a >= 0 and b >= 0 and a < self.height and b < self.length and grid[a][b] == island_char):
                self.dfs_mark_island(grid, a, b, to_mark, island_char)

    def numIslands(self, grid: list[list[str]]) -> int:
        self.length = len(grid[0])
        self.height = len(grid)
        nb_islands = 0
        island_char = '1'
        for i in range(self.height):
            for j in range(self.length):
                if grid[i][j] == island_char:
                    nb_islands += 1
                    self.dfs_mark_island(grid, i, j, '#', island_char)
                    print(grid)
        return (nb_islands)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
grid  = [["1","0","1","1","0","1","1"]]
sol = Solution()
print(sol.numIslands(grid))
print(grid)
