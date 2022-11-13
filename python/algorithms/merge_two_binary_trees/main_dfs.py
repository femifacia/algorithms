#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    def dfs(self, side1 : TreeNode, side2 : TreeNode, prec : TreeNode, side_int : int):
        if not side2:
            return
        if not side1:
            if (side_int):
                prec.right = side2
            else:
                prec.left = side2
            return
        side1.val += side2.val
        self.dfs(side1.left, side2.left, side1, 0)
        self.dfs(side1.right, side2.right, side1, 1)

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 == None:
            return root2
        if root2 == None:
            return root1
        root1.val += root2.val
        self.dfs(root1.left, root2.left, root1, 0)
        self.dfs(root1.right, root2.right, root1, 1)        
        return root1