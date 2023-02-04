#!/usr/bin/env python3

import math
import heapq
#from collections import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
#        arr = sorted(points,key=lambda p:)
        arr = [(math.sqrt((p[1] **2) + (p[0] ** 2)), [p[0], p[1]]) for p in points]
        heapq.heapify(arr)
#        print(arr)
        return [heapq.heappop(arr)[1] for p in range(k)]


sol = Solution()
points = [[50,1], [10, 3], [4,4], [90,-2]]
k = 1
points = [[3,3],[5,-1],[-2,4]]
k = 2
points = [[1,3],[-2,2]]
k = 2
print(sol.kClosest(points,k))