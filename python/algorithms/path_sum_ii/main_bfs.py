#!/usr/bin/env python3

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def pathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return []
        
        to_see = deque([(root, root.val, [])])
        ans = []
        while (to_see):
            current, val, arr = to_see.pop()
            if not current.left and not current.right and val == targetSum:
                ans.append(arr + [current.val])
            if current.left:
                to_see.appendleft((current.left, val + current.left.val, arr + [current.val]))
            if current.right:
                to_see.appendleft((current.right, val + current.right.val, arr + [current.val]))
        return ans