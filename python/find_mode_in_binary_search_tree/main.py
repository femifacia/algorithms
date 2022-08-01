#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def findModeNode(self, root, maxi, count_node, max_node):
        if (root == None):
            return (maxi)
        if (root.val in count_node):
            count_node[root.val] += 1
        else:
            count_node[root.val] = 1
        if (count_node[root.val] >= maxi):
            maxi = count_node[root.val]
            if (maxi in max_node):
                max_node[maxi].append(root.val)
            else:
                max_node[maxi] = [root.val]
        return (max(self.findModeNode(root.left, maxi, count_node, max_node), self.findModeNode(root.right, maxi, count_node, max_node)))
    def findMode(self, root) -> list[int]:
        if (root == None):
            return ([])
        count_node = {}
        max_node = {}
        maxi = self.findModeNode(root, 0, count_node, max_node)
        return(max_node[maxi])