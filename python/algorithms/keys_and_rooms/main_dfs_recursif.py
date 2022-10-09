#!/usr/bin/env python3

class Solution:

    def dfs(self, graph : list[list[int]], node : int, visited : dict) -> bool:
        visited[node] = 1
        if len(visited) == self.size:
            return True
        for neighbor in graph[node]:
            if (neighbor in visited):
                continue
            if self.dfs(graph, neighbor, visited):
                return True
        return (False)

    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        self.size = len(rooms)
        return (self.dfs(rooms, 0, {}))

sol = Solution()
rooms = [[2,3],[],[2],[1,3]]
rooms = [[1,3],[3,0,1],[2],[0]]
rooms = [[1],[2],[3],[]]
print(sol.canVisitAllRooms(rooms))