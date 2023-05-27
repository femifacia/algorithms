#!/usr/bin/env python3

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        k = 1
        to_see = deque([root])
        while (to_see):
            size = len(to_see)
            while size:
                size -= 1
                current = to_see.pop()
                if not current.left and not current.right:
                    return k
                if current.left:
                    to_see.appendleft(current.left)
                if current.right:
                    to_see.appendleft(current.right)
            k+=1
        return k