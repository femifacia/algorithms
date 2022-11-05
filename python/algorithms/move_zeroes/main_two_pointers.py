#!/usr/bin/env python3

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = nums.index(0) if 0 in nums else -1
        size = len(nums)
        if (right==-1 or right == size-1):
            return
        # left start from the frist 0. 
        left = right
        # right point toward the char after the next 0. 
        while (right < size and nums[right] == 0):
            right += 1
        while (left < right and right < size):
        # When nums[left] == 0 I swap it with nums[right] and right goes to the charactere after the next 0
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                while (right < size and nums[right] == 0):
                    right += 1
            left +=1

sol = Solution()
nums = [0,1,2,3000,0,0,0,-5,00,0,0,0,4,0,5,0,7,8]
print(nums)
sol.moveZeroes(nums)
print(nums)