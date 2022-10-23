#!/usr/bin/env python3

from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # So at the start I create two graph, graph_in and graph_out. 
        # Graph_in contains for a node i all nodes a,b,c… such as a → i , b →i, … are valid connections. 
        # Graph_out contains for a node i all nodes a,b,c… such as i ← , i ← b, … are valid connections. 
        graph_out = defaultdict(list)
        graph_in = defaultdict(list)
        for i,j in connections:
            graph_out[i].append(j)
            graph_in[j].append(i)
        nbr = 0
        #So I have an array connected_to_zerro  of n length. 
        # If a node i is connected to 0 connected_to_zerro[i] = 1 . 
        connected_to_zero = [-1] * n
        connected_to_zero[0] = 1
        #all in neighbors of 0 are put in 1 in my array connected_to_zero
        for i in graph_in[0]:
            connected_to_zero[i] = 1
        to_see = deque(graph_in[0])
        tmp = 1
        # So to start, I do a BFS to all in neighbors of 0. 
        while (to_see):
            current = to_see.pop()
            tmp +=1
            for i in graph_in[current]:
                if connected_to_zero[i] == 0:
        # Then I update their status in connected_to_zerro . 
                    connected_to_zero[i] = 1
                    to_see.appendleft(i)
        #if I count as much as connected values as n, I stop here. It means there is no need to reorder any route
        if (tmp == n):
            return 0
        # Since this step is done I start another BFS but applied to all neighbors of 0, in or out. 
        to_see = deque(graph_out[0] + graph_in[0])
        #print(connected_to_zero)
        while (to_see):
            current = to_see.pop()
        # For each current, I put he is connected to 0. 
            connected_to_zero[current] = 1
            is_connected = 0
        # To optimize the treatement, when I see a node before appending it I put its value to 0, 
        # so I only append value which are -1. This method avoid adding many times the same node.
            for i in graph_out[current]:
                if connected_to_zero[i] == 1:
                    is_connected = 1
                elif connected_to_zero[i] == -1:
                    connected_to_zero[i] = 0
                    to_see.appendleft(i)
        # Then I check if in its out connexion, if there is a node connected to 0. 
        # If not I increment nbr  variable which is the nbr of routes to reorder. 
            if is_connected == 0:
                nbr += 1
        # After that all its in neighbors never seen are added.
            for i in graph_in[current]:
                if connected_to_zero[i] == -1:
                    connected_to_zero[i] = 0
                    to_see.appendleft(i)
        #print("in", graph_in, "\nout", graph_out)
        #print(connected_to_zero)
        return nbr

sol = Solution()
n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
n = 3
connections = [[1,0],[2,0]]
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(sol.minReorder(n, connections))