#!/usr/bin/env python3

import math

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:

    def isGoodNode(self, root, root_val, greater):
        if root == None:
            return (0)
        res = 1 if (root.val >= root_val and root.val >= greater) else 0
        if (res):
            greater = root.val
        return res + self.isGoodNode(root.left, root_val, greater) + self.isGoodNode(root.right, root_val, greater)

    def goodNodes(self, root: TreeNode) -> int:
        if (root == None):
            return (0)
        return (self.isGoodNode(root.left, root.val, root.val) + 1 + self.isGoodNode(root.right, root.val, root.val))

sol = Solution()
node = TreeNode(9, TreeNode(1), TreeNode(2, TreeNode(10), TreeNode(15)))
print(sol.goodNodes(node))