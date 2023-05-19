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
        pred = prev
        stack = [None]
        while (index <= right):
            stack.append(current)
            current = current.next
            index += 1
        next_node = stack[-1].next
        current = stack.pop()
        reversed_head = current
        while (stack):
            current.next = stack.pop()
            prev = current
            current = current.next
        prev.next = next_node
        if (pred):
            pred.next = reversed_head
        if left == 1:
            head = reversed_head
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
printTree(sol.reverseBetween(l, 2,4))