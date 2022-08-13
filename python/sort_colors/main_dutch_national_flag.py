#!/usr/bin/env python3

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = mid = 0
        size = len(nums)
        high = size - 1
        while (mid <= high):
            if (nums[mid] == 0):
                nums[mid],nums[low] = nums[low], nums[mid]
                low += 1
            elif (nums[mid] == 2):
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
                mid -= 1
            mid +=1
sol = Solution()
arr = [2,0,2,1,1,0,1,2,0,1,1,1,1,0, 2]
print(arr)
sol.sortColors(arr)
print(arr)