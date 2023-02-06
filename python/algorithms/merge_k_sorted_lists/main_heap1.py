#!/usr/bin/env python3

import heapq

#This work on me but not on leetcode cause of the version of the heap and sort crap
#So this version consume less memory than the 2

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        size = len(lists)
        minHeap = []
#        heapq.heapify()
        current = None
        for elm in lists:
            current = elm
            while (current):
                heapq.heappush(minHeap, [current.val, current])
                current = current.next
        print(minHeap)
        head = heapq.heappop(minHeap)[1] if minHeap else None
        size = len(minHeap)
        current = head
        while (size >= 1):
            current.next = heapq.heappop(minHeap)[1]
            current = current.next
            size -= 1
        if size:
            heapq.heappop(minHeap)[1].next = None
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

printTree(sol.mergeKLists([None, ListNode(1), list1, list2]))