#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    def dfsInorder(self, root):
        if not root:
            return
        self.dfsInorder(root.left)
        self.mini = min(self.mini, abs(self.prev - root.val))
        self.prev = root.val
        self.dfsInorder(root.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        arr = []
        self.mini = float('inf')
        self.prev = float('inf')
        self.dfsInorder(root)
        return self.mini