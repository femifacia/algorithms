#!/usr/bin/env python3

from collections import deque


class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        if (graph == [[]]):
            return 0
        n = len(graph)
        #the queue containing nodes we will visit
        to_see = deque() 
        #this array of booleans contains n column and for each columns, 1 << n ( 2 ^ n)lines
        #this array will permit to see if for a node n, if we have already gain this node with a path mask
        #if it is, visited[n][mask] will be 1
        #because we have n nodes we have to set the number of lines to 1 << n because the biggest mask we will
        #have is (1 << n) - 1
        visited = [[0] * (1 << n) for i in range(n)]
        #and if we see a mask wich is equal to (1 << n) - 1 it means we have visited all paths. Then we have
        #to stop the program.
        end = (1 << n) - 1
        #let's take an example. If there are 4 nodes. end is (1 << 4) - 1 ==  1111.
        #So if a node has this path, it means we have already seen node 0; 1, 2, 3, 4
        #so we can stop the process

        #to count the path of the shortest path, we will use this variable steps
        #each generations, steps will increment by one.
        steps = 0

        #We will start the bfs using on the first generation, all nodes
        #to each nodes we add its value to the queue and the mask of the nodes seen.
        #the first node to see all nodes, (having mask equal to end)  will be the fastest

        #at the init state we associate to each node, its value as a mask.
        #so the 4th node will be associated to 10000 (1 << i)
        for i in range(n):
            to_see.appendleft((i, 1 << i))
        while (to_see):
            size = len(to_see)
            while (size):
                size -= 1
                current, mask = to_see.pop()
                #current is the actual  node
                #mask is the mask containing all nodes seen
                if mask == end:
                    return steps
                #if this node has already been visited using this mask it means we have done this path one time
                #then we just continue
                if visited[current][mask]:
                    continue
                visited[current][mask] = 1
                for neighbor in graph[current]:
                    to_see.appendleft((neighbor, mask | (1 << neighbor)))
            steps += 1
        #print(visited)

sol = Solution()
graph = [[1,2,3],[0],[0],[0]]
graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
print(sol.shortestPathLength(graph))