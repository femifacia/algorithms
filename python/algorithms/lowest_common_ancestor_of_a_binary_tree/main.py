#!/usr/bin/env python3
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right
     def __str__(self):
        return (str(self.val))

class Solution:

    def genealogie(self, root, elm):
        if (root == None):
            return None
        if (root.val == elm.val):
            return ([root])
        left = self.genealogie(root.left, elm)
        right = self.genealogie(root.right, elm)
        if (left):
            return [root] + left
        if (right):
            return [root] + right
        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        one = self.genealogie(root, p)
        two = self.genealogie(root, q)
        size_one = len(one) - 1
        size_two = len(two) - 1
        print(one)
        print(two)
        while (size_one > size_two):
            size_one -= 1
        while (size_two < size_one):
            size_two -= 1        
        while (size_one >= 0 and (one[size_one].val != two[size_one].val)):
            size_one -= 1
        if (size_one >= 0):
            return (one[size_one])
        return (None)

sol = Solution()
two = TreeNode(2)
three = TreeNode(3)
one = TreeNode(1, TreeNode(5, TreeNode(6, TreeNode(7), TreeNode(8))), three)
print(sol.lowestCommonAncestor(one, TreeNode(8), TreeNode(5)).val)