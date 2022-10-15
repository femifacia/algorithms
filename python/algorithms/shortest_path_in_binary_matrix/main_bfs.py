#!/usr/bin/env python3

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        dist = [[-1] * width for i in range(height)]
        to_see = deque([(height - 1, width - 1)]) if grid[height -1][height -1] == 0 else None
        dist[height - 1][width - 1] = 1 if to_see else -1
        while (to_see):
            i,j = to_see.pop()
            for i1, j1 in [(i + 1,j), (i, j + 1), (i- 1, j), (i, j-1), (i-1, j-1), (i+1,j+1), (i-1,j+1), (i+1,j-1)]:
                if 0 <= i1 < height and 0 <= j1 < width and dist[i1][j1] < 0 and grid[i1][j1] == 0:
                    dist[i1][j1] = dist[i][j] + 1
                    if (i1 == 0 and j1 == 0):
                        return dist[0][0]
                    to_see.appendleft((i1,j1))
#        [print(i) for i in dist]
        return dist[0][0]

sol = Solution()
grid = [[0,0,0],[1,1,0],[1,1,0]]
grid = [[0,1],[1,0]]
grid = [[1,0,0],[1,1,0],[1,1,0]]
print(sol.shortestPathBinaryMatrix(grid))