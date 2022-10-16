#!/usr/bin/env python3

# Definition for a binary tree node.


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    def traversal(self, root : TreeNode) -> None:
        if not root:
            return
        self.traversal(root.left)
        self.k -= 1
        if (self.k == 0):
            self.ans = root.val
            return
        self.traversal(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.traversal(root)
        return (self.ans)