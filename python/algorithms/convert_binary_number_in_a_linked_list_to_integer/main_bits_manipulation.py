#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while (head):
            res = (res << 1) | head.val
            head = head.next
        return res

sol = Solution()
head = ListNode(1, ListNode(0, ListNode(1)))
print(sol.getDecimalValue(head))