#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        to_see = [root]
        count = 0
        while (to_see):
            current = to_see.pop()
            count += 1
            if (current.left):
                to_see.append(current.left)
            if current.right:
                to_see.append(current.right)
        return count