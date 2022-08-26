#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = {}
        while (head):
            if head in seen:
                return (head)
            seen[head] = 1
            head = head.next
        return (None)