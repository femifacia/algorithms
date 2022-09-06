#!/usr/bin/env python3

import math

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:

    def isGoodNode(self, root, greater):
        if root == None:
            return (0)
        if (root.val >= greater):
            return 1 + self.isGoodNode(root.left, root.val) + self.isGoodNode(root.right, root.val)
        return self.isGoodNode(root.left, greater) + self.isGoodNode(root.right, greater)        

    def goodNodes(self, root: TreeNode) -> int:
        if (root == None):
            return (0)
        return (self.isGoodNode(root.left, root.val) + 1 + self.isGoodNode(root.right, root.val))

sol = Solution()
node = TreeNode(9, TreeNode(1), TreeNode(2, TreeNode(10), TreeNode(15)))
print(sol.goodNodes(node))