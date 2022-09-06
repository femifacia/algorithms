#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        arr = []
        i= 0
        tmp = head
        new_head = ListNode()
        new_tmp = new_head
        is_first = 1
        while (tmp != None):
            arr.append(tmp.val)
            i += 1
            tmp = tmp.next
            if (i % k == 0):
                while (arr):
                    if (not is_first):
                        new_tmp.next = ListNode()
                        new_tmp = new_tmp.next
                    new_tmp.val = arr.pop()
                    if (is_first):
                        is_first = 0
        for j in arr:
            if (not is_first):
                new_tmp.next = ListNode()
                new_tmp = new_tmp.next
            new_tmp.val = j
            if (is_first):
                is_first = 1
        return (new_head)

arr = list(map(int, input().split(" ")))
k = int(input())
head = ListNode()
tmp = head
size = len(arr)
for i in range(size):
    tmp.val = arr[i]
    if (i + 1 < size):
        tmp.next = ListNode()
        tmp = tmp.next
sol = Solution()
head = sol.reverseKGroup(head, k)
