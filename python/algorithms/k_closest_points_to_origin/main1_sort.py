#!/usr/bin/env python3

import math

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        arr = sorted(points,key=lambda p:math.sqrt((p[1] **2) + (p[0] ** 2)))
        return arr[0:k]


sol = Solution()
points = [[50,1], [10, 3], [4,4], [90,-2]]
k = 1
points = [[3,3],[5,-1],[-2,4]]
k = 2
points = [[1,3],[-2,2]]
k = 1
print(sol.kClosest(points,k))