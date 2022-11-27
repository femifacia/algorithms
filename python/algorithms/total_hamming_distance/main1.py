#!/usr/bin/env python3

#brut force not optimized

class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        maxx = max(nums)
        count = 0
        size = len(nums)
        for i in range(32):
            place = 1 << i
            for a in range(size):
                for b in range(a + 1, size):
                    if (place & nums[a]) != (place & nums[b]):
                        count += 1
            if place > maxx:
                return count
        return count
sol = Solution()
nums = [4,14,2]
nums = [0,1,1,0,0,1,1]
nums = [0,1,1,0,0,1,1]
print(sol.totalHammingDistance(nums))