#!/usr/bin/env python3

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #our snowball

        snowball = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                snowball +=1
            elif snowball > 0:
                nums[i], nums[i - snowball] = 0, nums[i]

sol = Solution()
nums = [0,1,2,3000,0,0,0,-5,00,0,0,0,4,0,5,0,7,8]
print(nums)
sol.moveZeroes(nums)
print(nums)