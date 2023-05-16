#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        left = right = head
        for i in range(1,k):
            right = right.next
        end_ptr = right
        while (right.next):
            left = left.next
            right = right.next
        end_ptr.val, left.val = left.val, end_ptr.val
        return head

def printList(head : ListNode):
    while (head):
        print(head.val, '->', end="")
        head = head.next
    print()

sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10, ListNode(11)))))))))))
head = ListNode(1, ListNode(2,ListNode(3, ListNode(4, ListNode(5)))))
head = ListNode(1, ListNode(2,ListNode(3)))
head = ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(7, ListNode(8, ListNode(3, ListNode(0, ListNode(9, ListNode(5))))))))))
head = ListNode(1, ListNode(2))


printList(sol.swapNodes(head, 2))