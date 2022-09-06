#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        while (head != None):
            arr.append(head)
            head = head.next
        arr.append(None)
        if (arr[-n - 1] == arr[0]):
            if (len(arr) == 2):
                return None
            arr[1].next = arr[2]
            return (arr[1])
        elif (arr[-n -1] == arr[-2]):
            arr[-3].next = None
            return arr[0]
        else:
            arr[-n -2].next = arr[-n]
            return (arr[0])