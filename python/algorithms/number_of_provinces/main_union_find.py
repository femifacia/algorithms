#!/usr/bin/env python3

class union_find:
    def __init__(self, n) -> None:
        #the parent array is an array for which for each i, parrent[i] is the its parent
        #at the begining all element are unconnected which means parrent[i] = i
        self.parent = [i for i in range(n)]
        #rank is the rang of a root. It is the rank which the tree would have if it weren't
        #compressed (the maximal depth)
        self.rank = [0] * n
        #the number of elements
        self.size = n
    
    def find(self, x):
        #we compress the path toward each parent by doing self.parent[x] = self.find(self.parent[x])
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if (parent_x == parent_y): #already linked
            return False
        if (self.rank[parent_x] == self.rank[parent_y]): #we only increment the rank of a node if we are facing
            #a node with the same rank.
            #remember, the rank is the maximal depth of a tree if there were no compression
            self.rank[parent_x] += 1
            self.parent[parent_y] = parent_x
        #we put the three with the lower rank under the one with the higher rank
        elif self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_x] = parent_y
        return True

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        nb_provinces = size = len(isConnected)
        uf = union_find(size)
        for i in range(size - 1):
            for j in range(size):
                if isConnected[i][j] and uf.union(i, j):
                    nb_provinces -= 1
        return nb_provinces

sol = Solution()
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(sol.findCircleNum(isConnected))