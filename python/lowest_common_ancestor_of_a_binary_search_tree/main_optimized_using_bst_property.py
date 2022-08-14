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
        while (1):
            if (q.val < root.val and p.val < root.val):
                root = root.left
            elif (q.val > root.val and p.val > root.val):
                root = root.right
            else:
                break
        return (root)

sol = Solution()
two = TreeNode(2)
three = TreeNode(3)
one = TreeNode(1, TreeNode(5, TreeNode(6, TreeNode(7), TreeNode(8))), three)
print(sol.lowestCommonAncestor(one, TreeNode(8), TreeNode(5)).val)