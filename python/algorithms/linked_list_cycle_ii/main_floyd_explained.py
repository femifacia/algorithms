#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        speed = head
        slow = head
        while (speed and speed.next):
            #we use floyd'cycle detection to find the meeting point of the list
            slow = slow.next
            speed = speed.next.next
            #when slow and speed are equal we found the point
            if (slow == speed and speed and speed.next):
                speed = head
                #since then, we set a pointer to the head of the list. I used speed to not have to declare 
                #a new variable
                while 1:
                #so we will loop on the pointer to the head and the slow pointer and wait to their encount
                #it is a mathematic law bruh.
                    if (head == speed):
                        return (head)
                    head = head.next
                    speed = speed.next
        return (None)