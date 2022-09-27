#!/usr/bin/env python3

from collections import deque

class Solution:

    def bfs(self, grid, rotten_orange, good_orange, height, width) ->int:
        time = -1
        to_see = deque(rotten_orange)
        while (to_see):
            size = len(to_see)
            for _ in range(size):
                i, j = to_see.pop()
                for i1, j1 in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= i1 < height and 0 <= j1 < width and grid[i1][j1] == 1:
                        grid[i1][j1] = 2
                        good_orange -= 1
                        to_see.appendleft((i1, j1))
            time += 1
        return -1 if good_orange else (time if time >= 0 else 0)

    def orangesRotting(self, grid: list[list[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        rotten_orange = []
        good_oranges = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    rotten_orange.append((i,j))
                elif grid[i][j] == 1:
                    good_oranges += 1
        return (self.bfs(grid, rotten_orange, good_oranges, height, width))

grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]
sol = Solution()
print(sol.orangesRotting(grid))