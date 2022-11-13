#!/usr/bin/env python3

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

#Not mine lol

class Solution:
    def connect(self, root):
        if not root: return None
        L, R, N = root.left, root.right, root.next
        if L:
            L.next = R
            if N: R.next = N.left
            self.connect(L)
            self.connect(R)
        return root
