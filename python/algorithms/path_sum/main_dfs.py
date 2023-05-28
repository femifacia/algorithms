#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root : TreeNode, path : int, target : int) -> None:
        path += root.val
        if path == target and not root.left and not root.right:
            self.ans = True
            return
        if not self.ans and root.left:
            self.dfs(root.left, path, target)
        if not self.ans and root.right:
            self.dfs(root.right, path, target)

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        self.ans = False
        self.dfs(root,0 ,targetSum)

        return self.ans