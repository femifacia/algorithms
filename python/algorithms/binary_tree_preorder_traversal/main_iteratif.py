#!/usr/bin/env python3

from inspect import stack


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root) -> list[int]:
        if (root == None):
            return ([])
        result = []
        stack = [root]
        while (stack):
            node = stack.pop()
            result.append(node.val)
            if (node.right):
                stack.append(node.right)
            if (node.left):
                stack.append(node.left)
        return (result)
                