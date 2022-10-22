#!/usr/bin/env python3

from collections import Counter
import itertools

class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        if roads == []:
            return 0
        if n == 2:
            return 1
        graph = {}
        res = 0
        for i, j in roads:
            graph[i] = graph.get(i, []) + [j]
            graph[j] = graph.get(j, []) + [i]
        for city1, city2 in itertools.combinations(graph.keys(), 2):
            has_connection = 1 if city1 in graph[city2] else 0
            res = max(res, len(graph[city1]) + len(graph[city2]) - has_connection)
#        print("a", a)
#        print(len(roads))
#        print(i,j)
        return res
sol = Solution()

n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
n = 8
roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
n = 5
roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
roads = [[1,0]]
n = 2
n = 10
roads = [[7,1],[9,7],[9,4],[0,6],[1,3],[2,0],[8,2],[6,1],[3,8],[0,7],[0,4],[4,6],[2,7],[4,3],[5,9],[1,0],[5,2],[0,8],[8,9],[3,9],[8,6],[3,7],[2,3],[6,2],[3,5],[5,4],[7,4],[2,9],[9,1],[7,8],[4,1],[8,5],[2,1],[3,6],[5,7],[6,9],[6,7],[0,5],[1,8],[3,0],[8,4]]
n = 8
roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
print(sol.maximalNetworkRank(n, roads))