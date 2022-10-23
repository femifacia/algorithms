#!/usr/bin/env python3

from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:


        # So at the start I create two graph, graph_in and graph_out. 
        # Graph_in contains for a node i all nodes a,b,c… such as a → i , b →i, … are valid connections. 
        # Graph_out contains for a node i all nodes a,b,c… such as i ← , i ← b, … are valid connections. 
        #Due to the statement of the exercise, we are sure that a node has only 
        # one connection (if you read the constraints you will get it). 
        # So this exercise can be understanded such as, For each outgoing edge I have to do a reverse operation
        # So here again I create graph_in and graph_out. 
        graph_out = defaultdict(list)
        graph_in = defaultdict(list)
        for i,j in connections:
            graph_out[i].append(j)
            graph_in[j].append(i)
        nbr = 0
        seen = [0] * n
        seen[0] = 1
        to_see = deque([0])

        # I start from 0. 
        while (to_see):
            current = to_see.pop()
            for i in graph_out[current]:
        # All outgoing nodes are reversed (I increment nbr) and I add them to the queue. 
                if seen[i] == 0:
                    seen[i] = 1
                    to_see.appendleft(i)
                    nbr += 1
        # Then I add all ingoing connexion and do the thing until the graph is over
            for i in graph_in[current]:
                if seen[i] == 0:
                    seen[i] = 1
                    to_see.appendleft(i)
        return nbr

sol = Solution()
n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
n = 3
connections = [[1,0],[2,0]]
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(sol.minReorder(n, connections))