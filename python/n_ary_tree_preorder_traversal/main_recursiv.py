#!/usr/bin/env python3


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def dfs(self, root, res):
        if (root == None):
            return
        res.append(root.val)
        for i in root.children:
            self.dfs(i, res)

    def preorder(self, root: 'Node') -> list[int]:
        res = []
        if (root == None):
            return ([])
        self.dfs(root, res)
        return (res)