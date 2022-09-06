#!/usr/bin/env python3

from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if (root == None):
            return ([])
        res = []
        que = deque()
        que.append(root)
        while (que):
            # we pop the rightest value  from the tree 
            right = que.pop()
            res.append(right.val)
            size = len(que)
            while (size):
                #for each value of the previous level we add its left side and its right side
                #so at the end of this loop we will have the all nodes of this level
                tmp = que.popleft()
                if (tmp.left):
                    que.append(tmp.left)
                if (tmp.right):
                    que.append(tmp.right)
                size-=1
            # we also add the left and right side of the previous rightest node
            if (right.left):
                que.append(right.left)
            if (right.right):
                que.append(right.right)
        return (res)