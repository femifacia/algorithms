#!/usr/bin/env python3


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        if (root == None):
            return ([])
        to_see = [root]
        res = []
        while (to_see):
            curr = to_see.pop()
            res.append(curr.val)
            if curr.children:
                for j in curr.children:
                    to_see.append(j)
        return (res[::-1])