#!/usr/bin/env python3

class Solution:

#count, size
#time exceed

    def isBound(self, arr, minK, maxK) -> bool:
        if min(arr) == minK and max(arr) == maxK:
            return True
        return False

    def howManySubarrays(self, arr, minK, maxK, i) -> int:
        count = 0
        size = 0
        for j in range(i + 1, self.size + 1):
            if self.isBound(arr[i:j], minK, maxK):
                count = count + 1
            elif count:
                return count
        return count

    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        count = 0
        self.size = len(nums)
        for i in range(len(nums)):
            print(i, count)
            count += self.howManySubarrays(nums, minK, maxK, i)
        return count

sol = Solution()
nums = [1,1,1,1]
mink = 1
maxk = 1


nums = [35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913]
mink = 35054
maxk = 945315
nums = [1,3,5,2,7,5,1,1]
mink = 1
maxk = 5
print(sol.countSubarrays(nums, mink, maxk))