#!/usr/bin/env python3

class union_find:

    #this function apply a find to all element on the uf structure
    #so after this we are ensured that all connections done lately are well integrated to their
    #far root

    def update(self) -> None:
        for i in range(self.size):
            self.find(i)

    def __init__(self, n) -> None:
        #the parent array is an array for which for each i, parrent[i] is the its parent
        #at the begining all element are unconnected which means parrent[i] = i
        self.parent = [i for i in range(n)]
        #rank is the rang of a root. It is the rank which the tree would have if it weren't
        #compressed (the maximal depth)
        self.rank = [0] * n
        #the number of elements
        self.size = n
        self.useless_cables = 0
    
    def find(self, x):
        #we compress the path toward each parent by doing self.parent[x] = self.find(self.parent[x])
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if (parent_x == parent_y): #already linked
            self.useless_cables += 1
            return False
        if (self.rank[parent_x] == self.rank[parent_y]): #we only increment the rank of a node if we are facing
            #a node with the same rank.
            #remember, the rank is the maximal depth of a tree if there were no compression
            self.rank[parent_x] += 1
            self.parent[parent_y] = parent_x
        elif self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_x] = parent_y
        return True

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        uf = union_find(n)
        for i,j in connections:
            uf.union(i,j)
#        print(uf.useless_cables)
        uf.update()
        movement = len(set(uf.parent)) - 1
        #print(movement)
        #print("uf", uf.parent)
        return movement if uf.useless_cables >= movement else - 1


sol = Solution()
n = 6
connections = [[0,1],[0,2],[0,3],[1,2]]
n = 4
connections = [[0,1],[0,2],[1,2]]
n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
n = 5
connections = [[0,1],[0,2],[3,4],[2,3]]
print(sol.makeConnected(n, connections))