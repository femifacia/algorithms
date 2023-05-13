#!/usr/bin/env python3

# time O(n)
# space O(n)

class Solution:
    def firstMissingPositive(self, nums):
        # the solution is in the interval [1, len(nums) + 1]
        # so we will transform nums to a set and request for the numbers from 1 to len(nums + 2)
        # to see which numb is not in the set

        # cause the request of finding an elm in a set is constant we have an 0(n) solution
        nums = set(nums)
        for i in range(1, len(nums) + 2):
            if not i in nums:
                return i


        
sol = Solution()
arr = [1,2,4,3,-100]
print(sol.firstMissingPositive(arr))