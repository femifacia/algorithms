#!/usr/bin/env python3

from collections import deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        res = 0
        graph = [[] for i in range(n)]
        for i in range(n):
            if (i == headID):
                continue
            graph[manager[i]] += [i]
        to_see = deque([(headID, informTime[headID])])
        while (to_see):
            current_boss, current_time = to_see.pop()
            res = max(res, current_time)
            for sub in graph[current_boss] :
                to_see.appendleft((sub, current_time + informTime[sub]))
        return res