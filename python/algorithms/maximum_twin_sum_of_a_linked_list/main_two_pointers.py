#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:

    def reverseList(self, head : ListNode) -> ListNode:
        current = head
        prev = None
        while (current):
            old_next = current.next
            current.next = prev
            prev = current
            current = old_next
        return prev

    def pairSum(self, head: ListNode) -> int:
        fast = head
        slow = head
        val = 0
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        slow = self.reverseList(slow)
        while (slow):
            val = max(slow.val + head.val, val)
            slow = slow.next
            head = head.next
        return val

sol = Solution()
head = ListNode(5,ListNode(4, ListNode(2, ListNode(1))))
print(sol.pairSum(head))