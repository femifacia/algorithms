#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def dfs(self, root : TreeNode, path : str) -> None:
        if not root.left and not root.right:
            self.ans.append(path + str(root.val))
            return
        if root.left:
            self.dfs(root.left, path + str(root.val) +"->")
        if root.right:
            self.dfs(root.right, path + str(root.val) +"->")
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        self.ans = []
        self.dfs(root, "")
        return self.ans