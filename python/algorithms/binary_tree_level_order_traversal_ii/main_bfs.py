#!/usr/bin/env python3

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        to_see = deque([root])
        res = []
        while to_see:
            size = len(to_see)
            tmp = []
            while size:
                size -= 1
                current = to_see.pop()
                if current.left:
                    to_see.appendleft(current.left)
                if current.right:
                    to_see.appendleft(current.right)
                tmp.append(current.val)
            res.append(tmp)
        return res[::-1]