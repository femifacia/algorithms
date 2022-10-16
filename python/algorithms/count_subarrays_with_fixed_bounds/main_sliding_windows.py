#!/usr/bin/env python3

class Solution:

#count, size
#time exceed



    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        count = 0
        isMin = 0
        isMax = 0
        startOfSubarray = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                isMin = isMax = 0
                startOfSubarray = i + 1
                continue
            if nums[i] == minK:
                isMin = 1
                i_min = i
            if nums[i] == maxK:
                isMax = 1
                i_max = i
            if (isMin and isMax):
                count += (min(i_min, i_max) - startOfSubarray + 1)
            #count += self.howManySubarrays(nums, minK, maxK, i)
        return count

sol = Solution()

nums = [35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913]
mink = 35054
maxk = 945315
nums = [1,3,5,2,7,5,1,1]
mink = 1
maxk = 5
nums = [1,1,1,1]
mink = 1
maxk = 1
print(sol.countSubarrays(nums, mink, maxk))