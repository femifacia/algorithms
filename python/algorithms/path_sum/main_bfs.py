#!/usr/bin/env python3

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        to_see = deque([(root, root.val)])

        while (to_see):
            current, val = to_see.pop()
            if not current.left and not current.right and val == targetSum:
                return True
            if current.left:
                to_see.appendleft((current.left, val + current.left.val))
            if current.right:
                to_see.appendleft((current.right, val + current.right.val))
        return False