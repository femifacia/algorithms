#!/usr/bin/env python3
from collections import defaultdict, deque


class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        graph = defaultdict(list)
        n = len(edges)
        for i in range(n):
            if (edges[i] != -1):
                graph[i].append(edges[i])
        seen_node1 = [0] * n
        seen_node2 = [0] * n
        to_see_1 = deque([node1])
        to_see_2 = deque([node2])
        seen_node1[node1] = 1
        seen_node2[node2] = 1
        while (to_see_1 or to_see_2):
            current1 = to_see_1.pop() if to_see_1 else None
            current2 = to_see_2.pop() if to_see_2 else None
            print(current1, current2)
            if current1 != None and current2 != None and seen_node2[current1] and seen_node1[current2]:
                return (min(current1, current2))
            if current2 != None and seen_node1[current2]:
                return current2
            if  current1 != None and seen_node2[current1]:
                return current1
            for neighbor in graph[current1]:
                if not seen_node1[neighbor]:
                    seen_node1[neighbor] = 1
                    to_see_1.appendleft(neighbor)
            for neighbor in graph[current2]:
                if not seen_node2[neighbor]:
                    seen_node2[neighbor] = 1
                    to_see_2.appendleft(neighbor)
        return -1

sol = Solution()
edges = [2,2,3,-1]
node1 = 0
node2 = 1
edges = [1,2,-1]
node1 = 0
node2 = 2
edges = [2, 0, 0]
node1 = 2
node2 = 0
edges = [51,-1,75,17,71,-1,52,15,58,44,16,22,47,4,60,71,32,10,84,-1,51,51,17,-1,15,51,32,53,83,83,47,-1,67,-1,47,6,46,77,9,-1,-1,61,11,54,6,15,7,37,8,0,9,81,30,49,38,-1,-1,22,68,48,-1,80,36,36,-1,22,52,48,82,27,68,10,56,84,32,49,75,57,77,50,36,9,61,0,49,0,16]
node1 = 27
node2 = 22
print(sol.closestMeetingNode(edges, node1, node2))        