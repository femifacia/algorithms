#!/usr/bin/env python3

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        j = 1
        k = 2
        size = len(nums)
        while (k < size):
            if nums[i] != nums[j] or nums[j] != nums[k]:
                return (nums[i])
            i+=3
            j+=3
            k+=3
        return nums[i]

nums = [99,99,-4,0,1,0,1,0,1,99]
nums = [1]
sol = Solution()
print(sol.singleNumber(nums))