#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    def dfs(self, root) -> int :
        if (root == None):
            return (False)
        left  = self.dfs(root.left)
        right = self.dfs(root.right)
        if left == False:
            root.left = None
        if right == False:
            root.right = None
        return ((left or right or root.val))

    def pruneTree(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        if (root.left == None and root.right == None and root.val == 0):
            return (None)
        return root
    
def preorder(root):
    if root ==  None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

node = TreeNode(0, TreeNode(1), TreeNode(0, TreeNode(0)))
sol = Solution()
sol.pruneTree(node)
preorder(node)