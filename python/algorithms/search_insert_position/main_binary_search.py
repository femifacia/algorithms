#!/usr/bin/env python3

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return right + 1

sol = Solution()
nums = [1,3,5,6]
target = 6
print(sol.searchInsert(nums, target))