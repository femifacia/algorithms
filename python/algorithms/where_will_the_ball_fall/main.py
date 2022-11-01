#!/usr/bin/env python3

class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        height = len(grid)
        width = len(grid[0])
        ans = [-1] * width
        position = [i for i in range(width)]
        ball = [i for i in range(width)]
        ans = 0
        i = 0
        while (ans != width and i < height):
            for j in position:
                if ball[j] != -1:
                    if 0 <= ball[j] + grid[i][ball[j]] < width and grid[i][ball[j]] + grid[i][ball[j] + grid[i][ball[j]]] != 0:
                        ball[j] += grid[i][ball[j]]
                    else:
                        ball[j] = -1
                        ans += 1
            i += 1
        return ball

sol = Solution()
grid = [[-1]]
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
print(sol.findBall(grid))