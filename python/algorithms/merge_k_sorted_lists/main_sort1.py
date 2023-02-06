#!/usr/bin/env python3

import heapq

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        sortedArr = []
        current = None
        for elm in lists:
            current = elm
            while (current):
                sortedArr.append([current.val, current])
                current = current.next
        sortedArr.sort(key = lambda x : x[0])
        print(sortedArr)
        head = sortedArr[0][1] if sortedArr else None
        i = 0
        size = len(sortedArr)
        while (i + 1 < size):
            current = sortedArr[i][1]
            current.next = sortedArr[i+1][1]
            i+=1
        if size:
            sortedArr[-1][1].next = None
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