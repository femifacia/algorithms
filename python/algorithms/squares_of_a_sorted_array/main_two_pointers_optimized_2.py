#!/usr/bin/env python3

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        ans = [0] *(right + 1)
        i = right
        left_num, right_num = nums[left] ** 2, nums[right] **2
        while left <= right:
            if (right_num >= left_num):
                ans[i] = right_num
                right-=1
                right_num = nums[right] ** 2
            else:
                ans[i] = left_num
                left += 1
                left_num = nums[left] ** 2
            i-=1
        return (ans)

nums = [4,5,-9,7,9,10, -50]
sol = Solution()
nums.sort()
print(sol.sortedSquares(nums))