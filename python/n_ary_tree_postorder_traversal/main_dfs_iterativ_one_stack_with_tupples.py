#!/usr/bin/env python3


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        res = []
        if (root == None):
            return ([])
        to_see = [(root, False)]
        while (to_see):
            curr, is_visited = to_see.pop()
            if (is_visited):
                res.append(curr.val)
            else:
                to_see.append((curr , True))
                if curr.children:
                    for j in range(len(curr.children) - 1, -1, -1):
                        to_see.append((curr.children[j], False))
        return (res)