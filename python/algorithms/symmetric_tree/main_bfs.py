#!/usr/bin/env python3

from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        to_see = deque([root])
        while (to_see):
            size = len(to_see)
            level = []
            while (size):
                current = to_see.pop()
                if current.left:
                    level.append(current.left.val)
                    to_see.appendleft(current.left)
                else:
                    level.append(-200)
                if current.right:
                    level.append(current.right.val)
                    to_see.appendleft(current.right)
                else:
                    level.append(-200)
                size -= 1
            if level != level[-1::]:
                return False
        return True