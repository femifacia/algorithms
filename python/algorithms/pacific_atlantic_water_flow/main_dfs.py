#!/usr/bin/env python3

from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        self.height = len(heights)
        self.width = len(heights[0])
        pacific = [[0] * self.width  for i in range(self.height)]
        atlantic = [[0] * self.width  for i in range(self.height)]
        to_see = [(0, i) for i in range(self.width)]
        to_see += [(i, 0) for i in range(self.height)]
        hybrid = []
        #to_see += [(self.height - 1, i) for i in range(self.width)]
        while (to_see):
            i, j =  to_see.pop()
            pacific[i][j] = 1
            for i1, j1 in [(i + 1, j), (i, j + 1), (i - 1,j), (i, j - 1)]:
                if 0 <= i1 < self.height and 0 <= j1 < self.width and heights[i1][j1] >= heights[i][j] and pacific[i1][j1] == 0:
                    to_see.append((i1, j1))
        #[print(i) for i in pacific]
        to_see = [(i, self.width -1) for i in range(self.height)]
        to_see += [(self.height - 1, i) for i in range(self.width)]
        while (to_see):
            i, j =  to_see.pop()
            if (atlantic[i][j]):
                continue
            atlantic[i][j] = 1
            if (pacific[i][j]):
                hybrid.append([i, j])
            for i1, j1 in [(i + 1, j), (i, j + 1), (i - 1,j), (i, j - 1)]:
                if 0 <= i1 < self.height and 0 <= j1 < self.width and heights[i1][j1] >= heights[i][j] and atlantic[i1][j1] == 0:
                    to_see.append((i1, j1))
        return hybrid


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
heights = [[1]]
sol = Solution()
print(sol.pacificAtlantic(heights))