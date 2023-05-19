#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        val = 0
        while (current):
            if  current.next and current.next.val == current.val:
                val = current.val
                while current and current.val == val:
                    current = current.next
                if (prev):
                    prev.next = current
                else:
                    head = current
            else:
                prev = current
                current = current.next
        return head