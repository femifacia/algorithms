#!/usr/bin/env python3

from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        blueGraph = defaultdict(list)
        redGraph = defaultdict(list)
        graphArr = [redGraph, blueGraph]
        graphIndx = [1,0]
        to_see = deque()
        blue_seen = [0] * (n + 1)
        red_seen = [0] * (n + 1)
        seenArr = [red_seen, blue_seen]
        ans = [-1] * n
        ans[0] = 0
        for i, j in redEdges:
            redGraph[i].append(j)
        for i, j in blueEdges:
            blueGraph[i].append(j)
        for i in redGraph[0]:
            ans[i] = 1
            red_seen[i] = 1
            to_see.append((i, 1, 0))
        for i in blueGraph[0]:
            blue_seen[i] = 1
            ans[i] = 1
            to_see.append((i, 1, 1))
        while (to_see):
            current, dist, graph = to_see.pop()
            for i in graphArr[graphIndx[graph]][current]:
                if ans[i] == -1:
                    ans[i] = dist + 1
                if seenArr[graphIndx[graph]][i] == 0:
                    seenArr[graphIndx[graph]][i] = 1
                    to_see.append((i, dist + 1, graphIndx[graph]))
        return (ans)

sol = Solution()
n = 3
redEdges = [[0,1],[1,2]]
blueEdges = []
n = 3
redEdges = [[0,1]]
blueEdges = [[1,2]]
n = 5
redEdges = [[0,1],[1,2],[2,3],[3,4]]
blueEdges = [[1,2],[2,3],[3,1]]
n = 3
redEdges = [[0,1],[0,2]]
blueEdges = [[1,0]]
print(sol.shortestAlternatingPaths(n, redEdges, blueEdges))