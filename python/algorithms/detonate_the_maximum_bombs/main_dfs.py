#!/usr/bin/env python3

from collections import defaultdict
import math

class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        graph = defaultdict(list)
        ans = 0
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                x = (bombs[i][0] - bombs[j][0]) ** 2
                y = (bombs[i][1] - bombs[j][1]) ** 2
                d = math.sqrt(x + y)
                if d <= bombs[i][2]:
                    graph[i].append(j)
        for i in range(len(bombs)):
            seen = {i}
            to_see = [i]
            while to_see:
                current = to_see.pop()
                for neighbor in graph[current]:
                    if not neighbor in seen:
                        to_see.append(neighbor)
                        seen.add(neighbor)
                ans = max(ans, len(seen))
        return ans


sol = Solution()
bombs = [[1,1,5],[10,10,5]]
bombs = [[2,1,3],[6,1,4]]
bombs = [[1,1,100000],[100000,100000,1]]
print(sol.maximumDetonation(bombs))