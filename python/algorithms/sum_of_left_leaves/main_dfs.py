#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    def dfs(self, root : TreeNode, isLeft : bool) -> None:
        if root == None:
            return
        if isLeft and root.left == None and root.right == None:
            self.sum += root.val
            return
        self.dfs(root.left, True)
        self.dfs(root.right, False)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        self.dfs(root.left, True)
        self.dfs(root.right, False)
        return self.sum