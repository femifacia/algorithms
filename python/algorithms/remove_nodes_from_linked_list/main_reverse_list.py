#!/usr/bin/env python3

import math

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

    def removeNodes(self, head: ListNode) -> ListNode:

        # I reverse the list one time, then When I found a current.val bigger than the previous maximum
        # I link this previous and the actual current
        # And at the end a reverse the list again
        head = self.reverseList(head)
        maximum = -math.inf
        current = head
        prev = None

        while (current):
            tmp_next = current.next
            if current.val >= maximum:
                maximum = current.val
                if (prev):
                    prev.next = current
                    current.next = None
                else:
                    head.next = None
                prev = current
            current = tmp_next
        return self.reverseList(head)

def printList(head : ListNode) -> None:
    while head:
        print(head.val,'-> ', end="")
        head = head.next
    print("")

sol = Solution()
head = ListNode(5,ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
printList(sol.removeNodes(head))