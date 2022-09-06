#!/usr/bin/env python3

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        sah = 0
        for i in nums:
            if (i - count > 0):
                count += (i - count)
            else:
                continue
            sah += 1
            if nums[-1] - count <= 0:
                break
        return (sah)

sol = Solution()
print(sol.minimumOperations([1,5,0,3,5]))
print(sol.minimumOperations([1,1,1,2,2,2,3,3]))
print(sol.minimumOperations([1,2,3,5]))