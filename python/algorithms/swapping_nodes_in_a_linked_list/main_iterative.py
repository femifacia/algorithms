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
        current = head
        arr = []
        while (current):
            arr.append(current)
            current = current.next

        # be carefull. The order of action is important
        # We have to replace the next of the prev of our targets before replacing their next
        # to avoid cycle creation if the index == len(arr) // 2  
        if k > 1:
            arr[k-2].next = arr[-k]
        if k < len(arr):
            arr[-k - 1].next = arr[k-1]

        old_next = arr[k-1].next
        arr[k-1].next = arr[-k].next
        arr[-k].next = old_next

        # we could have put the following line instead of the 3 lines above
#        arr[-k].next,arr[k-1].next = arr[k-1].next,arr[-k].next

        arr[-k], arr[k-1] = arr[k-1], arr[-k]
        return arr[0]

def printList(head : ListNode):
    while (head):
        print(head.val, '->', end="")
        head = head.next
    print()

sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
head = ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(7, ListNode(8, ListNode(3, ListNode(0, ListNode(9, ListNode(5))))))))))


printList(sol.swapNodes(head, 5))