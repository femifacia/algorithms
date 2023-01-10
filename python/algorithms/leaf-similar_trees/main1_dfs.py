#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def dfs(self, root : TreeNode, leaf : list[int]) -> None:
        if not root:
            return
        if not root.left and not root.right:
            leaf.append(root.val)
        else:
            self.dfs(root.left, leaf)
            self.dfs(root.right, leaf)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf1 = []
        leaf2 = []
        self.dfs(root1, leaf1)
        self.dfs(root2, leaf2)
        return leaf1 == leaf2