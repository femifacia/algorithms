#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    def dfs(self, root, arr):
        if not root:
            return
        self.dfs(root.left, arr)
        arr.append(root.val)
        self.dfs(root.right,arr)

    def getMinimumDifference(self, root: TreeNode) -> int:
        arr = []
        self.dfs(root, arr)
        mini = float('inf')
        for i in range(len(arr) - 1):
            mini = min(abs(arr[i] - arr[i + 1]), mini)
        return mini