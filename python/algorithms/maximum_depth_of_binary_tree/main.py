#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getMaxDepthSide(self, node, size):
        if (node == None):
            return (size)
        left = self.getMaxDepthSide(node.left, size + 1)
        right = self.getMaxDepthSide(node.right, size + 1)
        if (left > right):
            return (left)
        return (right)

    def maxDepth(self, root) -> int:
        if (root == None):
            return (0)
        left =  self.getMaxDepthSide(root.left, 1)
        right = self.getMaxDepthSide(root.right, 1)
        if (left > right):
            return (left)
        return (right)