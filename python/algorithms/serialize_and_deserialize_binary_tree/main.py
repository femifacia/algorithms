#!/usr/bin/env python3

# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Codec:

    def serialize(self, root : TreeNode) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = ""
        to_see = deque([root])
        while (to_see):
            current = to_see.pop()
            if (not current):
                tree += "None,"
                continue
            tree += (str(current.val) + ",")
            to_see.appendleft(current.left)
            to_see.appendleft(current.right)
        return tree
        

    def deserialize(self, data : str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #arr = list(filter(lambda x : x and x != None, data.split(',')))
        arr = list(map(lambda x: None if x == "None" else int(x), data.split(',')[:-1]))
        if (arr[0] == None):
            return None
        print(arr)
        arr = [0] + arr
        node = TreeNode(arr[1])
        current = node
        to_see = deque([node])
        i = 0
        for i in range(len(arr)):
            #print(i, numb)
            if (to_see):
                current = to_see.pop()
            if not current:
                continue
            current.left = TreeNode(arr[(i + 1) * 2]) if arr[(i + 1) * 2] != None else None
            current.right = TreeNode(arr[((i + 1 )* 2) + 1]) if arr[((i + 1) * 2) + 1] != None else None
            to_see.appendleft(current.left)
            to_see.appendleft(current.right)            
        return node

def preorder(root : TreeNode):
    if (not root):
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
        

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(5, TreeNode(4, None, TreeNode(2, TreeNode(5))), TreeNode(3))
print(ser.serialize(root))
ans = deser.deserialize(ser.serialize(root))
print("systemw")
preorder(root)
print("mein")
preorder(ans)