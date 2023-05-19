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
        
sol = Solution()
list1 = ListNode(0)
list2 = ListNode(100)
list1.next = ListNode(10, ListNode(20, ListNode(40, ListNode(360, ListNode(425)))))
list2.next = ListNode(200, ListNode(300, ListNode(400)))
list1 = ListNode(10, ListNode(20, ListNode(30)))
def printTree(liste):
    while (liste):
        print(liste.val, end="")
        if (liste.next):
            print("->", end="")
        else:
            print("")
        liste = liste.next

print("Before")
printTree(list1)
print("after")
printTree(sol.reverseList(list1))
