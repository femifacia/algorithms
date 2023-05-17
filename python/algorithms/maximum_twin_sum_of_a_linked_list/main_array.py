#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def pairSum(self, head: ListNode) -> int:
        arr = []
        while (head):
            arr.append(head.val)
            head = head.next
#        print(arr)
#        print(max(([i for i in range(len(arr) // 2)]), key=act))
        index = max([i for i in range(len(arr) // 2)], key = lambda x : arr[x] + arr[len(arr) - x -1])
        return arr[index] + arr[len(arr) - index - 1]

sol = Solution()
head = ListNode(5,ListNode(4, ListNode(2, ListNode(1))))
print(sol.pairSum(head))