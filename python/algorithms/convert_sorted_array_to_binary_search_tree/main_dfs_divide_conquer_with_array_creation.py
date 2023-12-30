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
    
    def insertRight(self, root, nums):
        if not nums:
            return
            #root.left = TreeNode(i)
        child = TreeNode(nums[len(nums) // 2])
        root.right = child
        left = nums[0:len(nums) // 2]
        right = nums[(len(nums) // 2) + 1:]
        self.insertLeft(child, left)
        self.insertRight(child, right)
    
    def insertLeft(self, root, nums):
        if not nums:
            return
            #root.left = TreeNode(i)
        child = TreeNode(nums[len(nums) // 2])
        root.left = child
        left = nums[0:len(nums) // 2]
        right = nums[(len(nums) // 2) + 1:]
#        print("left",left,right)
        self.insertLeft(child, left)
        self.insertRight(child, right)
    
    def insertToBst(self, i, root):
        if i < root.val:
            self.insertLeft(i, root)
        elif i > root.val:
            self.insertRight(i,root)
    
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root = TreeNode(nums[len(nums) // 2])
        left = nums[0:len(nums) // 2]
        right = nums[(len(nums) // 2) + 1:]
#        print(left,right)
        self.insertLeft(root, left)
        self.insertRight(root, right)
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