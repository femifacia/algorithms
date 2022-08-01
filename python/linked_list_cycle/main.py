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
        dic = {}
        while (head):
            if head in dic:
                return True
            dic[head] = 1
            head = head.next
        return (False)