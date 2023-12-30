#!/usr/bin/env python
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def insertBST(start,end,nums):
            if not start < end:
                return None
            middle = (start + end) // 2
            child = TreeNode(nums[middle])
            child.left = insertBST(start, middle,nums)
            child.right = insertBST(middle + 1, end, nums)
            return child
        if not nums:
            return None
        return insertBST(0, len(nums),nums)