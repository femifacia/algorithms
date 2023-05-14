#!/usr/bin/env python3

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        to_see = [root]
        prec = None
        while (to_see):
            current = to_see.pop()
            if current.right:
                to_see.append(current.right)
            if current.left:
                to_see.append(current.left)
            if prec:
                prec.right = current
                prec.left = None
            prec = current


def printBfs(root : TreeNode):
    to_see = deque([root])
    while (to_see):
        size = len(to_see)
        while (size):
            current = to_see.pop()
            print(current.val, '-', end='')
            if current.left:
                to_see.appendleft(current.left)
            if current.right:
                to_see.appendleft(current.right)
            size -= 1
        print()

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6)))
printBfs(root)
sol = Solution()
sol.flatten(root)
print('After')
printBfs(root)

