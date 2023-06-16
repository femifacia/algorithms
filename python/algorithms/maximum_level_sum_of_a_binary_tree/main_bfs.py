#!/usr/bin/env python3

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 1
        tmp_sum = 0
        max_sum = float('-inf')
        to_see = deque([root])
        count = 1
        while (to_see):
            size = len(to_see)
            tmp_sum = 0
            while(size):
                size-=1
                current = to_see.pop()
                tmp_sum += current.val
                if current.left:
                    to_see.appendleft(current.left)
                if current.right:
                    to_see.appendleft(current.right)
            if tmp_sum > max_sum:
                max_sum = tmp_sum
                level = count
            count += 1
        return level