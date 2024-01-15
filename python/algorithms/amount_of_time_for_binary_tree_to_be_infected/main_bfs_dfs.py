#!/usr/bin/env python

# Definition for a binary tree node.

from typing import Optional
from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_dic = {}
        self.start_node = None
        ans = -1

        def dfs(root : TreeNode, parent):
            if not root:
                return
            parent_dic[root.val] = parent
            if root.val == start:
                self.start_node = root
            if  self.start_node == None:
                dfs(root.left, root)
                dfs(root.right, root)
        
        dfs(root,None)
        to_see = deque([self.start_node])
        seen = set()
        while to_see:
            size = len(to_see)
            while size:
                tmp = to_see.pop()
                seen.add(tmp)
                if tmp.left and tmp.left not in seen:
                    to_see.appendleft(tmp.left)
                if tmp.right and tmp.right not in seen:
                    to_see.appendleft(tmp.right)
                if tmp.val in parent_dic and parent_dic[tmp.val]  and parent_dic[tmp.val] not in seen:
                    to_see.appendleft(parent_dic[tmp.val])
                size -= 1
            ans += 1
        
        return ans
        