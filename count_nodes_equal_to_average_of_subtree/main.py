#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def count_average(self,root):
        count = 0
        n = 1
        if (root == None):
            return (0, 0)
        countl, nl = self.count_average(root.left)
        countr, nr = self.count_average(root.right)
        if (root.left == None and root.right == None):
            return (root.val, 1)
        return (countl + countr + root.val, nl + nr + 1)
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = 0
        count = 0
        summ = 0
        if (root == None):
            return (0)
        ans += self.averageOfSubtree(root.left)
        ans += self.averageOfSubtree(root.right)
        if (root.left == None and root.right == None):
            #summ, count = self.count_average(root)
            #print(root.value)
            #if (summ / count == root.value):
            #    ans += 1
            return (1)
        summ, count = self.count_average(root)
        summ += root.val
        if (summ / count == root.val):
            ans += 1
        return (ans)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def count_average(self,root):
        count = 0
        n = 1
        if (root == None):
            return (0, 0)
        countl, nl = self.count_average(root.left)
        countr, nr = self.count_average(root.right)
        if (root.left == None and root.right == None):
            return (root.val, 1)
        return (countl + countr + root.val, nl + nr + 1)
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = 0
        count = 0
        summ = 0
        if (root == None):
            return (0)
        ans += self.averageOfSubtree(root.left)
        ans += self.averageOfSubtree(root.right)
        if (root.left == None and root.right == None):
            #summ, count = self.count_average(root)
            #print(root.value)
            #if (summ / count == root.value):
            #    ans += 1
            print(root.val, "sah")
            return (1)
        summ, count = self.count_average(root)
        #summ += root.val
        calc = float(summ / (count + 0))
        if (calc == float(root.val)):
            print(root.val)
            print(summ, "count", count, "hum", calc, float(root.val))
            ans += 1
        if (root.val == 4):
            print("finallll", summ, count)
        return (ans)