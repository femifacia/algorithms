#!/usr/bin/env python3

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        size = 1
        for level in range(0, len(triangle) -1):
            i = 0
            #a simple bfs.
            while (i < size):
                if i != 0 and triangle[level][i] < triangle[level][i - 1]:
                    triangle[level + 1][i] -= triangle[level][i-1]
                    triangle[level + 1][i] += triangle[level][i]
                elif i == 0:
                    triangle[level + 1][i] += triangle[level][i]
                triangle[level + 1][i + 1] += triangle[level][i]
                i += 1
            size += 1
        return min(triangle[-1])

sol = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
print(sol.minimumTotal(triangle))