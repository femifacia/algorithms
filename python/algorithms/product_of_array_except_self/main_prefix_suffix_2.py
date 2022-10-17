#!/usr/bin/env python3

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        prefix = 1
        suffix = 1
        #here we set all val of res with its prefix and At the end
        # we multiply each values of res by the suffix
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))