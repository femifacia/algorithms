#!/usr/bin/env python3

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        prefix = 1
        suffix = 1
        #i do the same thing than the main with prefix optimized but in one loop
        #sah
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            res[-i - 1] *= suffix
            suffix *= nums[-i -1]
        return res

sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))