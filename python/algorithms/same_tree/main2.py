#!/usr/bin/env python3

class Solution:
    def isSameNode(self, p, q, checker) -> bool:
        if (checker[0] == 0):
            return False
        if (p == q  and p == None):
            return True
        if (p == None or q == None):
            checker[0] = 0
            return False
        if (p.val != q.val):
            checker[0] = 0
            return False
        return (self.isSameNode(p.left, q.left, checker) and self.isSameNode(p.right, q.right, checker))
    def isSameTree(self, p, q) -> bool:
        checker = [1]
        return (self.isSameNode(p, q, checker))