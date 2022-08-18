#!/usr/bin/env python3

from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if (root == None):
            return  ([])
        arr = []
        tree = deque()
        tree.append(root)
        while (tree):
            size = len(tree)
            level = []
            for i in range(size):
                tmp = tree.popleft()
                level.append(tmp.val)
                if (tmp.left):
                    tree.append(tmp.left)
                if (tmp.right):
                    tree.append(tmp.right)
            arr.append(level)
        return (arr)

sol = Solution()
node = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sol.levelOrder(node))