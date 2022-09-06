#!/usr/bin/env python3

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #space complecity O(n)
        #time complexity O(n)

        size = len(nums)
        k = k % size
        if (size == 1 or k == 0):
            return
        cop = nums.copy()
        for i in range(k, size):
            nums[i] = cop[i - k]
        for i in range (0, k):
            nums[i] = cop[size - k + i]

sol = Solution()
arr=[1,2,3,4,5,6,7]
arr=[-1,-100,3,99]
print(arr)
sol.rotate(arr, 3)
print(arr)
        