#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if (not head.next):
            return None
        if  not head.next.next:
            head.next = None
            return head
        real_head = head
        fast = slow = head
        while (fast and fast.next):
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return real_head