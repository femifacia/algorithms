#!/usr/bin/env python3

# Definition for a binary tree node.
from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        to_see = deque([root])
        nums = []
        while (to_see):
            current = to_see.pop()
            nums.append(current.val)
            if current.right:
                to_see.appendleft(current.right)
            if (current.left):
                to_see.appendleft(current.left)
        nums.sort()
        return (nums[k - 1])