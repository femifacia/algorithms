#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while (head and head.val == val):
            head = head.next
        point = head.next if head else None
        prev = head
        while (point):
            if point.val == val:
                prev.next = point.next
                point = point.next
                continue
            prev = point
            point = point.next
        return (head)