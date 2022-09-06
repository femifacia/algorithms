#!/usr/bin/env python3

# Definition for a binary tree node.
from audioop import reverse


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    
    def dfs(self, root, row, col, dic):
        if (root == None):
            return
        if col not in dic:
            dic[col] = {}
            dic[col][row] = [root.val]
        else:
            dic[col][row] = dic[col].get(row, []) + [root.val]
            #dic[col][row].sort()
        self.min_col = min(self.min_col, col)
        self.max_col = max(self.max_col, col)
        self.dfs(root.left, row + 1, col - 1, dic)
        self.dfs(root.right, row + 1, col + 1, dic)
    
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        dic = {}
        res = []
        self.min_col = 0
        self.max_col = 0
        self.dfs(root, 0, 0, dic)
        for i in range(self.min_col, self.max_col + 1):
#            dic[i].sort()
            tmp = []
            for j in sorted(dic[i]):
                #print(sorted(dic[i][j]))
                tmp += sorted((dic[i][j]))
            res.append(tmp)
        return (res)
sol = Solution()
node = TreeNode(0, TreeNode(8), TreeNode(1, TreeNode(3, None, TreeNode(4, None, TreeNode(7))), TreeNode(2, TreeNode(5, TreeNode(6)), None)))
print(sol.verticalTraversal(node))