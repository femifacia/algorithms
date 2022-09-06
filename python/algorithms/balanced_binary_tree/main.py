#!/usr/bin/env python3

# Definition for a binary tree node.
from turtle import right


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def heigtTree(self, root, height):
        if (root == None):
            return (height)
        left = self.heigtTree(root.left, height + 1)
        right = self.heigtTree(root.right, height + 1)
        if (left < 0 or right < 0):
            return -1
        if (left > right and left - right > 1):
            return -1
        elif (right > left and right - left > 1):
            return (-1)    
        return max(left, right)
    
    def isBalanced(self, root: TreeNode) -> bool:
        if (not root):
            return (True)
        left = self.heigtTree(root.left, 0)
        right = self.heigtTree(root.right, 0)
        if (left < 0 or right < 0):
            return (False)
        if (left > right and left - right > 1):
            return False
        if (right > left and right - left > 1):
            return False
        return (True)