#!/usr/bin/env python3

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        ans = []
        while left <= right:
            #left_num, right_num = nums[left] ** 2, nums[right] **2
            if (abs(nums[right]) > abs(nums[left])):
                ans = [nums[right] ** 2] + ans
                right-=1
            else:
                ans = [nums[left] ** 2] + ans
                left += 1
        return (ans)

nums = [4,5,-9,7,9,10, -50]
sol = Solution()
nums.sort()
print(sol.sortedSquares(nums))