#!/usr/bin/env python3


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        if (root == None):
            return ([])
        to_see = [root]
        res = []
        while (to_see):
            curr = to_see.pop()
            res.append(curr.val)
            #we append children from the most left to the most right
            #so when we unpopit the order is parent ,right, left
            if curr.children:
                for j in curr.children:
                    to_see.append(j)
        #we return the stack reversed so at the end it is, left, right, parent
        return (res[::-1])