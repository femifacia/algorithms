#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        speed = head
        sah = head
        while (speed and speed.next):
            head = head.next
            speed = speed.next.next
            if (head == speed and speed and speed.next):
                speed = sah
                while 1:
                    if (head == speed):
                        return (head)
                    head = head.next
                    speed = speed.next
        return (None)