#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        if (head == None):
            return (None)
        tmp_next = head.next
        head.next = None
        while (tmp_next):
            tmp_next_next = tmp_next.next
            tmp_next.next = head
            head = tmp_next
            tmp_next= tmp_next_next
        return (head)

    def isPalindrome(self, head: ListNode) -> bool:
        if (head == None):
            return (True)
        fast = slow = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        slow = self.reverseList(slow)
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