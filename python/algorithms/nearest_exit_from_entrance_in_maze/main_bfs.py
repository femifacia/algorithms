#!/usr/bin/env python3

from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        to_see = deque()
        height = len(maze)
        width = len(maze[0])
        to_see.appendleft((entrance[0], entrance[1], 0))
        while (to_see):
            #print(to_see)
            i, j, dist = to_see.pop()
            for i1, j1 in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= i1 < height and 0 <=  j1 < width:
                    if maze[i1][j1] == '.':
                        maze[i1][j1] = 1
                        to_see.appendleft((i1, j1, dist + 1))
                elif (i, j) != (entrance[0], entrance[1]):
                    #print(i1, j1, dist)
                    return dist
        return -1

sol = Solution()
maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]
maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]
maze = [[".","+"]]
entrance = [0,0]
[print(i) for i in maze]
print(sol.nearestExit(maze, entrance))