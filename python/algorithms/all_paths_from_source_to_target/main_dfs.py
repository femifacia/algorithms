#!/usr/bin/env python3

class Solution:

    def dfs(self, graph : list[list[int]], node : int, target : int, visited: dict) -> list[list[int]]:
        if (node == target):
            return [[target]]
        visited[node] = 1
        paths = []
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            path = self.dfs(graph, neighbor, target, visited)
            for i in path:
                paths.append([node] + i)
        visited.pop(node)
        return paths

    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        paths = []
        size = len(graph)
        source = 0
        target = size - 1
        visited = {source : 1}
        for neighbor in graph[source]:
            path = self.dfs(graph, neighbor, target, visited) 
            for i in path:
                paths.append([source] + i)
        return paths

sol = Solution()
graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(sol.allPathsSourceTarget(graph))