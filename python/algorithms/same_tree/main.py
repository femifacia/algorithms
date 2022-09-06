#!/usr/bin/env python3

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if (p == q  and p == None):
            return True
        if (p == None or q == None):
            return False
        if (p.val != q.val):
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))