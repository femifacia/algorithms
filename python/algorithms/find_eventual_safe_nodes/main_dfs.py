#!/usr/bin/env python3

class Solution:

    def isSafeNode(self, node, graph) -> bool:

        #when a node don't lead to safe node I put it to -1
        #if already seen to 2 so if I found a same node two time a return -1
        #else I put 1
        if self.SafeNode[node] == -1:
            return False
        if (self.SafeNode[node] == 2):
            self.SafeNode[node] = -1
            return False
        if (self.SafeNode[node] == 1):
            return True
        self.SafeNode[node] = 2
        for i in graph[node]:
            if self.isSafeNode(i, graph) == False:
                self.SafeNode[i] = -1
                self.SafeNode[node] = -1
                return False
        self.SafeNode[node] = 1
        return True

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        self.SafeNode = [0] * n
        res = []
        for i in range(n):
            if ((self.SafeNode[i] == 1)):
                res.append(i)
            elif (self.SafeNode[i] == 0 and self.isSafeNode(i, graph)):
                res.append(i)
        return res

sol = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(sol.eventualSafeNodes(graph))