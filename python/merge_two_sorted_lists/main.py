#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if (list1 == None):
            return (list2)
        if (list2 == None):
            return (list1)
        (head, other) = (list1, list2) if (list1.val < list2.val) else (list2, list1)
        current = head
        while (current and other):
            while (current.next and other and current.next.val > other.val):
                tmp_current_next = current.next
                tmp_other_next = other.next
                current.next = other
                other.next = tmp_current_next
                other = tmp_other_next
            if (current.next == None):
                current.next = other
                break
            current = current.next
        return (head)
sol = Solution()
list1 = ListNode(0)
list2 = ListNode(100)
list1.next = ListNode(10, ListNode(20, ListNode(40, ListNode(360, ListNode(425)))))
list2.next = ListNode(200, ListNode(300, ListNode(400)))

def printTree(liste):
    while (liste):
        print(liste.val, end="")
        if (liste.next):
            print("->", end="")
        else:
            print("")
        liste = liste.next

printTree(sol.mergeTwoLists(list2, list1))