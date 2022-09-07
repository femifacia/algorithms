#!/usr/bin/env python3
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if (root == None):
            return ""
        string = str(root.val)
        if (root.left or (root.right)):
            string +=  "("
            string += self.tree2str(root.left)
            string += ")"
        if root.right:
            string +="("
            string += self.tree2str(root.right)
            string += ")"
        return (string)

node = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
sol = Solution()
print(sol.tree2str(node))