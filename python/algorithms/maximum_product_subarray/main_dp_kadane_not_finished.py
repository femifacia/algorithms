#!/usr/bin/env python3

#DONT WORKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKk

import sys

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        dp_plus = [1] * len(nums)
        dp_minus = [1] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                dp_plus[i] = nums[i] * max(1, dp_plus[i-1])
                dp_minus[i] = nums[i] * dp_minus[i-1] if dp_minus[i-1] != 0 else nums[i]
            elif nums[i] < 0:
                dp_minus[i] = dp_minus[i-1] * nums[i] if dp_minus[i-1] != 0 else nums[i]
                dp_plus[i] = max(nums[i], dp_minus[i])
                if dp_minus[i] > 0:
                    dp_minus[i] = nums[i]
            else:
                dp_plus[i] = 0
                dp_minus[i] = 0
        print(dp_plus)
        print(dp_minus)
        return max(dp_plus)

sol = Solution()
nums = [int(i) for i in sys.argv[1:]]
print(sol.maxProduct(nums))