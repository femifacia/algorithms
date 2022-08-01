#!/usr/bin/env python3
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def postorderTraversal(self, root) -> list[int]:
        if (root == None):
            return ([])
        return (self.postorderTraversal(root.left) +  self.postorderTraversal(root.right) + [root.val])

    
sol = Solution()
four = TreeNode(4)
three = TreeNode(3)
two = TreeNode(2, four)
one = TreeNode(1, two, three)
print(sol.postorderTraversal(one))