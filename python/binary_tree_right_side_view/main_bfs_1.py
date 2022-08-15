#!/usr/bin/env python3

from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if (root == None):
            return ([])
        res = []
        que = deque()
        que.append(root)
        while (que):
            size = len(que)
            while (size):
                rightest = que.popleft()
                if (rightest.left):
                    que.append(rightest.left)
                if (rightest.right):
                    que.append(rightest.right)
            res.append(rightest.val)
        return (res)