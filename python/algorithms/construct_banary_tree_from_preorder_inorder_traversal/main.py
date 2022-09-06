#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    def buildTree(self, preorder: list[int], inorder: list[int]):
        print("pre", preorder, "in", inorder)
        if (preorder == []):
            return (None)
        val = preorder[0]
        node = TreeNode(val)
        index_cut = inorder.index(val)
        print("index", index_cut)
        node.left = self.buildTree(preorder[1:index_cut + 1], inorder[0:index_cut])
        node.right = self.buildTree(preorder[index_cut + 1:], inorder[index_cut + 1:])
        return (node)

def preTraversal(node):
    if (node == None):
        return
    print(node.val)
    preTraversal(node.left)
    preTraversal(node.right)


def postTraversal(node):
    if (node == None):
        return
    postTraversal(node.left)
    postTraversal(node.right)
    print(node.val)


def inTraversal(node):
    if (node == None):
        return
    inTraversal(node.left)
    print(node.val)
    inTraversal(node.right)

sol = Solution()
preTraversal(sol.buildTree([3,9,20,15,7], [9,3,15,20,7]))