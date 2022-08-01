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

    def postorderTraversal(self, root) -> list[int]:
        if (root == None):
            return ([])
        result = []
        dum = TreeNode(0, root)
        first = None
        middle = None
        last = None
        current = dum
        while (current):
            if (current.left):
                predecessor = self.findPredecessor(current)
                if (predecessor.right == None):
                    predecessor.right = current
                    current = current.left
                else:
                    first = current
                    middle = current.left
                    while (current != middle):
                        last = middle.right
                        middle.right = first
                        first = middle
                        middle = last
                    first = current
                    middle = predecessor
                    while (current != middle):
                        result.append(middle.val)
                        last = middle.right
                        middle.right = first
                        first = middle
                        middle = last
                    predecessor.right = None
                    current = current.right
            else:
                current = current.right
        return (result)

sol = Solution()
four = TreeNode(4)
three = TreeNode(3)
two = TreeNode(2, four)
one = TreeNode(1, two, three)
print(sol.postorderTraversal(one))