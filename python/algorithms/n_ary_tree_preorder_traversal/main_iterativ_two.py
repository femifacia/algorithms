#!/usr/bin/env python3


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        res = []
        if (root == None):
            return ([])
        to_see = [root]
        to_see_curr = []
        while (to_see):
            curr = to_see.pop()
            res.append(curr.val)
            if curr.children:
                for j in curr.children:
                    to_see_curr = [j] + to_see_curr
                to_see += to_see_curr
                to_see_curr = []
        return (res)