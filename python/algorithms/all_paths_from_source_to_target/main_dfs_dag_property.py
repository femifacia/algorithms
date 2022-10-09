#!/usr/bin/env python3

class Solution:

    
    def dfs(self, graph : list[list[int]], node : int, target : int) -> list[list[int]]:
        if (node == target):
            return [[target]]
        paths = []
        for neighbor in graph[node]:
            path = self.dfs(graph, neighbor, target)
            for i in path:
                paths.append([node] + i)
        return paths

    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        paths = []
        size = len(graph)
        source = 0
        target = size - 1
        for neighbor in graph[source]:
            path = self.dfs(graph, neighbor, target) 
            for i in path:
                paths.append([source] + i)
        return paths