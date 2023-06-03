#!/usr/bin/env python3

from collections import deque
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        ans = 0
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)
        to_see = deque([(headID,0)])
        while to_see:
            current, time = to_see.pop()
            time += informTime[current]
            ans = max(time, ans)
            for neighbor in graph[current]:
                to_see.appendleft((neighbor, time))
        return ans