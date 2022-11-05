#!/usr/bin/env python3

from collections import defaultdict
import math

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
#        dic = defaultdict(int)
        idx = -1
        value = math.inf
        dist = 0
        for i in range(len(points)):
            if points[i][0] != x and points[i][1] != y:
                continue
            dist = abs(points[i][0] - x) + abs(points[i][1] - y)
            if (dist < value):
                #if i found a 0 I return it immediatly cause it is the smallest distance we can find
                if dist == 0:
                    return i
                value = dist
                idx = i
        return (idx)
