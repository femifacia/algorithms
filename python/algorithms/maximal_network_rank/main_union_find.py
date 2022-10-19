#!/usr/bin/env python3

from collections import Counter


class union_find:

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
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        if roads == []:
            return 0
        if n == 2:
            return 1
        a = 0
        uf = union_find(n)
        for i, j in roads:
            if (not uf.union(i,j)):
                a += 1
            print(uf.parent)
        print("a", a)
        print(len(roads))
        uf.update()
        count = Counter(uf.parent)
        print(uf.parent)
        print(count)
        res = max(count.values())
        return (res) if res <= len (roads) else res - 1
sol = Solution()

n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
n = 8
roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
n = 5
roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
roads = [[1,0]]
n = 2
n = 10
roads = [[7,1],[9,7],[9,4],[0,6],[1,3],[2,0],[8,2],[6,1],[3,8],[0,7],[0,4],[4,6],[2,7],[4,3],[5,9],[1,0],[5,2],[0,8],[8,9],[3,9],[8,6],[3,7],[2,3],[6,2],[3,5],[5,4],[7,4],[2,9],[9,1],[7,8],[4,1],[8,5],[2,1],[3,6],[5,7],[6,9],[6,7],[0,5],[1,8],[3,0],[8,4]]
print(sol.maximalNetworkRank(n, roads))