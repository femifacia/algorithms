#!/usr/bin/env python3

# Definition for a binary tree node.
from collections import deque
import math


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = math.inf
        val = root.val
        to_see = deque([root])
        while (to_see):
            size = len(to_see)
            for _ in range(size):
                current = to_see.pop()
                if current.val != val:
                    res = min(current.val, res)    
                if current.left:
                    to_see.appendleft(current.left)
                if current.right:
                    to_see.appendleft(current.right)
        return res if res != math.inf else -1