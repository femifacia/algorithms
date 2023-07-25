#!/usr/bin/env python3

class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        ans = [-1] * len(nums)
        prefixSum = 0
        i = 0
        while i < k * 2 and i < len(nums):
            prefixSum += nums[i]
            i+=1
#        print(prefixSum)
        while i < len(nums):
            prefixSum +=  nums[i]
            ans[i - k] = prefixSum // (k * 2 + 1)
            prefixSum -= nums[i - 2 * k]
            i+=1
        return ans
    
sol = Solution()
nums = [8]
k = 100000
nums = [100000]
k = 0
nums = [7,4,3,9,1,8,5,2,6]
k = 3
print(sol.getAverages(nums, k))