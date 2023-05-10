#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traversal(self, root : TreeNode,low : int, high : int):
        if not root:
            return
        if (root.val <= high and root.val >= low):
            self.sum += root.val
        self.traversal(root.left, low, high)
        self.traversal(root.right, low, high)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        self.sum = 0
        self.traversal(root, low, high)
        return self.sum