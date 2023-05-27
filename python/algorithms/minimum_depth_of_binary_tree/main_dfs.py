#!/usr/bin/env python3


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs(self, root : TreeNode, k : int) -> None:
        if not root.left and not root.right:
            self.k = min(self.k, k)
            return
        #It will be a loose of time if we search for another depth if the actual depth is greater than self.k
        if root.left and k + 1 < self.k:
            self.dfs(root.left, k + 1)
        if root.right and k + 1 < self.k:
            self.dfs(root.right, k + 1)

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.k = float('inf')
        self.dfs(root, 1)
        return self.k