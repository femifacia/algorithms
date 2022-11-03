#!/usr/bin/env python3

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        ans = []
        left_num, right_num = nums[left] ** 2, nums[right] **2
        while left <= right:
            if (right_num >= left_num):
                ans = [right_num] + ans
                right-=1
                right_num = nums[right] ** 2
            else:
                ans = [left_num] + ans
                left += 1
                left_num = nums[left] ** 2
        return (ans)

nums = [4,5,-9,7,9,10, -50]
sol = Solution()
nums.sort()
print(sol.sortedSquares(nums))