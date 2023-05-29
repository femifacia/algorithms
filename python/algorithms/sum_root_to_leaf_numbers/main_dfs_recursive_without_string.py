#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root : TreeNode, numb : int ) -> None:
        if not root:
            return 0
        numb = numb * 10 + root.val
        if not root.left and not root.right:
            return numb
        return  self.dfs(root.left, numb) + self.dfs(root.right, numb) 

    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root,0)
