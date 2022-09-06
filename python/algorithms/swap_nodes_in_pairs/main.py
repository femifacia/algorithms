#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (head == None):
            return(None)
        arr = [None]
        current = head
        count = 0
        while (current):
            arr.append(current)
            tmp_next = current.next
            if (count == 1):
                #We relink the current and the previous
                current.next = arr[-2]
                arr[-2].next = tmp_next
                if (arr[-3]):
                    #if there is a previous to our previous node we link to our current
                    arr[-3].next = current
                #then we snap the current and the previous on our array
                tmp = arr[-2]
                arr[-2] = current
                arr[-1] = tmp
                count = -1
            current = tmp_next
            count += 1
        return (arr[1])

sol = Solution()
list1 = ListNode(0)
list2 = ListNode(100)
list1.next = ListNode(10, ListNode(20, ListNode(40, ListNode(360, ListNode(425)))))
list2.next = ListNode(200, ListNode(300, ListNode(400)))
list2 = None

def printTree(liste):
    while (liste):
        print(liste.val, end="")
        if (liste.next):
            print("->", end="")
        else:
            print("")
        liste = liste.next
print("Before")
printTree(list2)
print("after")
printTree(sol.swapPairs(list2))