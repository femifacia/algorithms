#!/usr/bin/env python3
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Solution:


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root == None or root == p or root == q):
            return (root)
        if (q.val < root.val and p.val < root.val):
            return (self.lowestCommonAncestor(root.left, p, q))
        if (q.val > root.val and p.val > root.val):
            return (self.lowestCommonAncestor(root.right, p, q))
        return (root)

sol = Solution()
two = TreeNode(2)
three = TreeNode(3)
one = TreeNode(1, TreeNode(5, TreeNode(6, TreeNode(7), TreeNode(8))), three)
print(sol.lowestCommonAncestor(one, TreeNode(8), TreeNode(5)).val)