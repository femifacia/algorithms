#!/usr/bin/env python

# We do the exact same thing than with the case of the sorted array to bst
# but we use two pointers skill to find the middle of the list

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
        if not head:
            return None
        tail = head
        while tail.next:
            tail = tail.next
        def insertBST(start,end,nums):
            if start == end:
                return None
            fast = start
            slow = start
            while fast != end and fast.next != end:
                fast = fast.next.next
                slow = slow.next
            middle = (start + end) // 2
            child = TreeNode(slow.val)
            child.left = insertBST(start, slow,nums)
            child.right = insertBST(slow.next, fast, nums)
            return child
        return insertBST(head,tail)