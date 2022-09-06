#!/usr/bin/env python3

from typing import List


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def findMinNode(self, lists, size):
        #findMiniNode and remove empty Nodes
        i = 0
        index = 0
        node = None
        while (i < size):
            if (lists[i]):
                if (node and lists[i].val < node.val):
                    node = lists[i]
                    index = i
                elif (not node):
                    node = lists[i]
                    index = i
                i += 1
            else:
                del lists[i]
                size -= 1
        if (index < size and lists[index]):
            lists[index] = lists[index].next
        return node, lists, size

    
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        #head = min elm
        size = len(lists)
        head, lists, size = self.findMinNode(lists, size)
        current = head
        #current->next = min elm
        while (current):
            current.next, lists, size = self.findMinNode(lists, size)
            current = current.next
        #return head
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

printTree(sol.mergeKLists([]))