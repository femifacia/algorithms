#!/usr/bin/env python3

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs(self, root : TreeNode) -> int:
        if not root:
            return 0
        val = root.val + self.dfs(root.left) + self.dfs(root.right)
        self.rank[val] += 1
        self.level_sum[self.rank[val]].append(val)
        self.maxi = max(self.rank[val], self.maxi)
        return val

    def findFrequentTreeSum(self, root:TreeNode) -> list[int]:
        self.level_sum = defaultdict(list)
        self.rank = defaultdict(int)
        self.maxi = 0
        self.dfs(root)
        return self.level_sum[self.maxi]