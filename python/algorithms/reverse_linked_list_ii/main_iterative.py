#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        prev = None
        current = head
        index = 1
        while (index < left):
            prev = current
            index += 1
            current = current.next
        reversed_head = current
        pred = prev
        while (index <= right):
            old_next = current.next
            current.next = prev
            prev = current
            current = old_next
            index += 1
        reversed_head.next = current
        if (pred):
            pred.next = prev
        if left == 1:
            head = prev
        return head

        
sol = Solution()
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
def printTree(liste):
    while (liste):
        print(liste.val, end="")
        if (liste.next):
            print("->", end="")
        else:
            print("")
        liste = liste.next
printTree(l)
printTree(sol.reverseBetween(l, 4,4))