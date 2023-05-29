#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def dfs(self, root : TreeNode, string : str):
        if not root.left and not root.right:
            self.words.append(chr(97 + root.val) + string)
            return
        if root.left:
            self.dfs(root.left, chr(97 + root.val) + string)
        if root.right:
            self.dfs(root.right,chr(97 + root.val) + string)

    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.words = []
        self.dfs(root, "")
        self.words.sort()
        return self.words[0]