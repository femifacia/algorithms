#!/usr/bin/env python3

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if (not root):
            return None
        to_see = deque([root])
        while (to_see):
            size = len(to_see) - 1
            prec = to_see.pop()
            if (prec.left):
                to_see.appendleft(prec.left)
            if (prec.right):
                to_see.appendleft(prec.right)
            while (size):
                current = to_see.pop()
                prec.next = current
                prec = current
                if (prec.left):
                    to_see.appendleft(prec.left)
                if (prec.right):
                    to_see.appendleft(prec.right)
                size -= 1
        return root
