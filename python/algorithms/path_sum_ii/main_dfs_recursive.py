#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root : TreeNode, path : int, target : int, arr : list) -> None:
        arr.append(root.val)
        path += root.val
        if path == target and not root.left and not root.right:
            self.ans.append(arr)
            return
        if root.left:
            self.dfs(root.left, path, target, arr + [])
        if root.right:
            self.dfs(root.right, path, target, arr + [])

    def pathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return []
        self.ans = []
        self.dfs(root,0 ,targetSum, [])

        return self.ans