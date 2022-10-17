#!/usr/bin/env python3

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = nums.copy()
        suffix = nums.copy()
        for i in range(1, len(nums)):
            prefix[i] *= prefix[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] *= suffix[i + 1]
        #I did prefix += [1] because of in my loop i have nums[i] = prefix[i-1] * suffix[i + 1]
        #So for i == 0 it is nums[0] = prefix[-1] * suffix[i]
        prefix = prefix + [1]
        suffix = suffix + [1]
        for i in range(len(nums)):
            nums[i] = prefix[i - 1] * suffix[i + 1]
        return nums

sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))