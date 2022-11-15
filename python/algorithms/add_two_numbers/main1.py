#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

#complexity 
# time : O(max(l1,l2)) in worst case
# space : O(1) 

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if ( not l2):
            return l1
        if not l1:
            return l2
        head1 = l1
        prec = None
        ret = 0
        while (l1 and l2):
            prec = l1
            l1.val = l1.val + l2.val + ret
            ret = 1 if l1.val >= 10 else 0
            l1.val %= 10
            l1 = l1.next
            l2 = l2.next
        while (l1 and ret):
            prec = l1
            l1.val += 1
            ret = 1 if l1.val >= 10 else 0
            l1.val %= 10
            l1 = l1.next
        if (l2):
            prec.next = l2
        while (l2 and ret):
            prec = l2
            l2.val += 1
            ret = 1 if l2.val >= 10 else 0
            l2.val %= 10
            l2 = l2.next
        if (ret):
            prec.next = ListNode(1) 
        return head1