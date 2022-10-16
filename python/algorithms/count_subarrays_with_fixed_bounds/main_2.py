#!/usr/bin/env python3

import math


class Solution:

#count, size
#time exceed

    def isBound(self, arr, minK, maxK) -> bool:
        #print("hehe", arr)
        if min(arr) == minK and max(arr) == maxK:
            return True
        return False

    def howManySubarrays(self, arr, minK, maxK, i, j) -> int:
        count = 0
        size = math.inf
        for j in range(j, self.size + 1):
            if self.isBound(arr[i:j], minK, maxK):
                count, size = count + 1, min(j - i - 1, size)
            elif count:
                return count, size
                #print(size)
        return count, size

    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        count = 0
        self.size = len(nums)
        i = 0
        size = 1
        while i < self.size:
            size = i + 1 if not size or size == math.inf else i + size
            tmp, size = self.howManySubarrays(nums, minK, maxK, i, size)
            #print(i, count, tmp, size)
            if (tmp):
                count += tmp
                i = i + 1
            else:
                i+= 1
        return count

sol = Solution()
nums = [1,1,1,1]
mink = 1
maxk = 1
mink = 78085
maxk = 995214
nums = [1,3,5,2,7,5,1,1]
mink = 1
maxk = 5
nums = [35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913]
mink = 35054
maxk = 945315
print(sol.countSubarrays(nums, mink, maxk))