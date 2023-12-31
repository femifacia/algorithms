#!/usr/bin/env python

# Definition for singly-linked list.

from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        tmp = head
        while tmp:
            nums.append(tmp.val)
            tmp = tmp.next
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
        return insertBST(0,len(nums),nums)