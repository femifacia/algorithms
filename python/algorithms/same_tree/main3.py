#!/usr/bin/env python3
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        if (p == q  and p == None):
            return True
        if (p == None or q == None or p.val != q.val):
            return False
        a = self.isSameTree(p.left, q.left)
        b = False if a == False else  self.isSameTree(p.right, q.right)
        return ( a and b)