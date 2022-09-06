#!/usr/bin/env python3

class Solution:

    def reverse(self, arr, i, j):
        while i < j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i+=1
            j-=1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #space complecity O(n)
        #time complexity O(1)

        size = len(nums)
        k = k % size
        if (size == 1 or k == 0):
            return
        self.reverse(nums, 0, size - 1 - k)
        self.reverse(nums, size - k, size - 1)
        self.reverse(nums, 0, size - 1)

sol = Solution()
arr=[-1,-100,3,99]
arr=[1,2,3,4,5,6,7]
print(arr)
sol.rotate(arr, 3)
print(arr)
        