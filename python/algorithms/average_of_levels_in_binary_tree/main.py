#!/usr/bin/env python3

# Definition for a binary tree node.
from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        to_see = deque()
        res = []
        to_see.append(root)
        while (to_see):
            size = len(to_see)
            nbr = 0
            for i in range(len(to_see)):
                curr = to_see.popleft()
                nbr += curr.val
                if (curr.left):
                    to_see.append(curr.left)
                if (curr.right):
                    to_see.append(curr.right)
            res.append(nbr / size)
        return (res)

sol = Solution()
node = TreeNode(3 , TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))
print(sol.averageOfLevels(node))