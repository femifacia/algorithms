#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head
        speed = head
        while (speed and speed.next):
            head = head.next
            speed = speed.next.next
        return (head)

sol = Solution()
node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(sol.middleNode(ListNode(1, ListNode(2))).val)
print(sol.middleNode(node).val)