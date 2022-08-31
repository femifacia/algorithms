#!/usr/bin/env python3


# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        res = []
        if (root == None):
            return ([])
        to_see = deque()
        to_see.append(root)
        while (to_see):
            level = []
            for i in range(len(to_see)):
                current = to_see.popleft()
                level.append(current.val)
                if current.children:
                    for j in current.children:
                        to_see.append(j)
            res.append(level)
        return (res)