#!/usr/bin/env python3

class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        maxx = max(nums)
        count = 0
        size = len(nums)
        for i in range(32):
            place = 1 << i
            count1 = 0
            for j in range(size):
                if (place & nums[j]):
                    count1 += 1
            count0 = size - count1
            #I noticed we could just do the product of the number of place where it is 1 by the number of
            #places where the bit is at 0
            count += (count0 * count1)
            if place > maxx:
                return count
        return count
sol = Solution()
nums = [0,1,1,0,0,1,1]
nums = [4,14,2]
print(sol.totalHammingDistance(nums))