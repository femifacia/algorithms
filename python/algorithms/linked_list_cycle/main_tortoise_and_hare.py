#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        speed = head
        while (speed and speed.next):
            head = head.next
            speed = speed.next.next
            if head == speed:
                return True
        return (False)