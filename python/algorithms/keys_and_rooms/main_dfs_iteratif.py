#!/usr/bin/env python3

class Solution:

    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        size = len(rooms)
        nbr_visited = 0
        visited = []
        to_see = [0]
        while (to_see):
            current = to_see.pop()
            if current in visited:
                continue
            nbr_visited += 1
            visited.append(current)
            for neighbor in rooms[current]:
                to_see.append(neighbor)
        return (nbr_visited == size)

sol = Solution()
rooms = [[1],[2],[3],[]]
rooms = [[2,3],[],[2],[1,3]]
rooms = [[1,3],[3,0,1],[2],[0]]
print(sol.canVisitAllRooms(rooms))