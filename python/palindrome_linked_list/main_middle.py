#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:

    def reverse(self, head):
        if (not head.next):
            return (head)
        tmp = self.reverse(head.next)
        tmp.next = head
        return (tmp)

    def isPalindrome(self, head: ListNode) -> bool:
        if (head == None):
            return (True)
        fast = slow = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        slow = self.reverse(slow)
        print(slow.val)
        while (slow):
            if (slow.val != head.val):
                return (False)
            slow = slow.next
            head = head.next
        return (True)

sol = Solution()
node = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(sol.isPalindrome(node))