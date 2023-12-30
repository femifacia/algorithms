#!/usr/bin/env python

# Definition for a binary tree node.

from typing import Optional
from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    
    def insertBST(self, root, start,end,nums, isRight):
        if not start < end:
            return
        middle = (start + end) // 2
        child = TreeNode(nums[middle])
        if not isRight:
            root.left = child
        else:
            root.right = child
        left_start = start
        left_end = middle
        right_start = middle + 1
        right_end = end
        self.insertBST(child, left_start, left_end, nums, 0)
        self.insertBST(child, right_start, right_end, nums, 1)
    
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        middle = len(nums) // 2
        root = TreeNode(nums[middle])
        left_start = 0
        left_end = len(nums) // 2
        right_start = (len(nums) // 2) + 1
        right_end = len(nums)

        self.insertBST(root, left_start, left_end, nums, 0)
        self.insertBST(root, right_start, right_end, nums, 1)
        return root
    
    def inorder(self, root : TreeNode):
        if not root:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)
    
    def levelOrder(self, root : TreeNode):
        if not root:
            return
        to_see = deque([root])
        print("levelllll orderrrr")
        while (to_see):
            size = len(to_see)
            while size:
                current = to_see.pop()
                print(current.val, end=" ")
                if current.left:
                    to_see.appendleft(current.left)
                if current.right:
                    to_see.appendleft(current.right)
                size -= 1
            print(" ")
        
root = TreeNode(0,TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(2)))
sol = Solution()
#sol.inorder(root)
nums = [-10,-3,0,4,5,9,11,20]
nums = [0,1,2,3,4,5]
root = sol.sortedArrayToBST(nums)
sol.inorder(root)
sol.levelOrder(root)