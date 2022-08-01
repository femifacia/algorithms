#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isValidNodeBST(self, root, mini, maxi) -> bool:
        if (root == None):
            return True
        if ((root.left != None and root.left.val >= root.val) or (root.right != None and root.right.val <= root.val)):
            return False
        if (mini and root.val <= mini):
            return (False)
        if (maxi and root.val >= maxi):
            return (False)
        return (self.isValidNodeBST(root.left, mini, root.val) and self.isValidNodeBST(root.right, root.val, maxi) == True)
    def isValidBST(self, root) -> bool:
        if (root == None):
            return True
        if ((root.left != None and root.left.val >= root.val) or (root.right != None and root.right.val <= root.val)):
            return False
        return (self.isValidNodeBST(root.left, None, root.val) and self.isValidNodeBST(root.right, root.val, None) == True)