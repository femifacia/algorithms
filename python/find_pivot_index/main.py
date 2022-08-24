#!/usr/bin/env python3

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        maxx = right = sum(nums[1:])
        if (right == 0):
            return (0)        
        i = 1
        size = len(nums)
        while (left != right and i + 1< size):
            left += nums[i-1]
            right -= nums[i]
            i+=1
        if (left != right and maxx + nums[0] - nums[-1] == 0):
            return (len(nums) - 1)
        return (i-1 if left == right else -1)

arr = [-1,-1,0,1,1,0]
sol = Solution()
print(sol.pivotIndex(arr))