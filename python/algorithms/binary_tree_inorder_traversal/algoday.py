#!/usr/bin/env python3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def inorderTraversal(root: TreeNode):
    if root == None:
        return
    inorderTraversal(root.left)
    print(root.val, end="->")
    inorderTraversal(root.right)

#we first print the left son of the root
#then we print the right son of the root
#and finally we print the root itself

root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2))

four = TreeNode(4)
three = TreeNode(3)
two = TreeNode(2, four)
one = TreeNode(1, two, three)

inorderTraversal(one)
root = None
inorderTraversal(root)

#we print at the first the left son of the node
#then we print the node itself
#and finally we print its right son
