#!/usr/bin/env python3


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneNode(self, node, dic):
        new_node = Node(node.val)
        dic[node.val] = new_node
        if not node.neighbors:
            return new_node
        new_node.neighbors = []
        for i in node.neighbors:
            neighbor = self.cloneNode(i, dic) if not i.val in dic else dic[i.val]
            new_node.neighbors.append(neighbor)
        return new_node

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        dic = {}
        return (self.cloneNode(node, dic))

sol = Solution()
sol.cloneGraph(Node(5))