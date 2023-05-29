#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root : TreeNode, path : int, digit : str) -> None:
        digit += str(root.val)
        if not root.left and not root.right:
            self.ans += int(digit)
            return
        if root.left:
            self.dfs(root.left, path, digit + "")
        if root.right:
            self.dfs(root.right, path, digit + "")

    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root,0 ,"")

        return self.ans