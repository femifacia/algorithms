#!/usr/bin/env python3

from collections import deque


class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        if (graph == [[]]):
            return 0
        n = len(graph)
        #the queue containing nodes we will visit
        to_see = deque() 
        #this is the dist array
        #this array of int contains n column and for each columns, 1 << n ( 2 ^ n)lines
        #this array will permit to see if for a node n, if we have already gain this node with a path mask
        #if it is, dist[n][mask] will be != than -1 and dist[n][mask] will contain the size of the path
        #because we have n nodes we have to set the number of lines to 1 << n because the biggest mask we will
        #have is (1 << n) - 1
        dist = [[-1] * (1 << n) for i in range(n)]
        #and if we see a mask wich is equal to (1 << n) - 1 it means we have visited all paths. Then we have
        #to stop the program.
        end = (1 << n) - 1
        #let's take an example. If there are 4 nodes. end is (1 << 4) - 1 ==  1111.
        #So if a node has this path, it means we have already seen node 0; 1, 2, 3, 4
        #so we can stop the process

        #We will start the bfs using on the first generation, all nodes
        #to each nodes we add its value to the queue and the mask of the nodes seen.
        #the first node to see all nodes, (having mask equal to end)  will be the fastest
        #we will put the dist of theses nodes to 0 such as dist[i][1 << i] = 0

        #at the init state we associate to each node, its value as a mask.
        #so the 4th node will be associated to 10000 (1 << i)
        for i in range(n):
            to_see.appendleft((i, 1 << i))
            dist[i][1 << i] = 0
        while (to_see):
            size = len(to_see)
            while (size):
                size -= 1
                current, mask = to_see.pop()
                #current is the actual  node
                #mask is the mask containing all nodes seen
                #if we have reached the end we return the dist of our current node, leaded by the mask
                if mask == end:
                    return dist[current][mask]
                for neighbor in graph[current]:
                    #if the neighbor has not been visited with the mask + the bit of the neighbor set to 1*
                    if dist[neighbor][mask | (1 << neighbor)] == -1:
                        #we add it to the queue
                        #then we set it dist to the dist of the courrent + 1
                        to_see.appendleft((neighbor, mask | (1 << neighbor)))
                        dist[neighbor][mask | (1 << neighbor)] = dist[current][mask] + 1

sol = Solution()
graph = [[1,2,3],[0],[0],[0]]
graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
print(sol.shortestPathLength(graph))