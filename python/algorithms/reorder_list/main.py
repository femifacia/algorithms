#!/usr/bin/env python3
import sys
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        while (head != None):
            arr.append(head)
            head = head.next
        size = len(arr)
        for i in range(size // 2):
            arr[i].next = arr[-1 -i]
            arr[-1 -i].next = arr[i + 1]
        arr[size // 2].next = None

head = ListNode(int(sys.argv[1]))
last = head
for i in range(2, len(sys.argv)):
    elm = ListNode(int(sys.argv[i]))
    last.next = elm
    last = elm
print("Before")
elm = head
while (elm != None):
    print(elm.val, end=",")
    elm = elm.next
print("")
sol = Solution()
sol.reorderList(head)
print("After")
elm = head
while (elm != None):
    print(elm.val, end = ",")
    elm = elm.next
print("")

print([5,6] == [6,5,])
