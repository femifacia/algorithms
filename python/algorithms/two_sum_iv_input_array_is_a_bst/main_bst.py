#!/usr/bin/env python3

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    #here we're gonna to use two pointers method

    def inorder_dfs(self, root : TreeNode, arr : list[int]) -> None:
        if root == None:
            return
        self.inorder_dfs(root.left, arr)
        arr.append(root.val)
        self.inorder_dfs(root.right, arr)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        arr = []
        #first we will parkour the three in dfs and stock it into an array

        #bst has particularities of beeing sorted arrays if read in inorder

        #so we will get all value inside this array

        self.inorder_dfs(root, arr)

        #then we will use two pointers method to find the sum such as array[left] + array[right] == k

        #if you are lost, look at the exercise two sum ii input as array sorted

        # I explained how to use two pointers to solve this problem
        left = 0
        right = len(arr) -1
        while (left < right):
            if arr[left] + arr[right] == k:
                return True
            if arr[left] + arr[right] < k:
                left += 1
            else:
                right -= 1
        return (False)