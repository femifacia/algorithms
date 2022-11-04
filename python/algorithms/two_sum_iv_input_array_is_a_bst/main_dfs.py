#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    def dfs(self, root, k) -> bool:
        if root == None:
            return False
        ret = k - root.val
        if (ret in self.dic):
            return True
        self.dic[root.val] = 1
        left = self.dfs(root.left, k)
        right = self.dfs(root.right, k)
        if (left):
            return left
        return right

    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.dic = {}
        return (self.dfs(root, k))