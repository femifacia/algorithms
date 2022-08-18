#!/usr/bin/env python3

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return (left)

sol = Solution()
arr = [0,5,9,8,7,6,2,1,4,52]
target=5
arr.sort()
print(arr)
print(sol.search(arr, target)) 