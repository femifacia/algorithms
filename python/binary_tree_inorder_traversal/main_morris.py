#!/usr/bin/env python3

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def findPredecessor(self, curr):
        current = curr.left
        while (current.right and current.right != curr):
            current = current.right
        return (current)

    def inorderTraversal(self, root) -> list[int]:
        if (root == None):
            return ([])
        result = []
        current = root
        while (current):
            if (current.left):
                predecessor = self.findPredecessor(current)
                if (predecessor.right == None):
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right
            else:
                result.append(current.val)
                current = current.right
        return (result)
    
sol = Solution()
four = TreeNode(4)
three = TreeNode(3)
two = TreeNode(2, four)
one = TreeNode(1, two, three)
print(sol.preorderTraversal(one))