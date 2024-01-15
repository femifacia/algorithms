#!/usr/bin/env python

from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        size = len(nums)
        res = 0
        # It is a math point
        n = size * (size - 1) // 2
        dp = {}
        for i in range(1, size):
            # We will create a 2D dp array such as dp[i][diff] is the number of
            # subsequence ending at i with diff
            dp[i] = defaultdict(int)
            for j in range(i):
                # We will scan every single value before i
                diff = nums[i] - nums[j]
                # if it was already a subsequence with the same diff as now on j
                # we will include it
                old = dp[j][diff] if j in dp else 0
                dp[i][diff] += (1 + old)
        for i in dp:
            # we do the sum of every subsequence even the ones which has not a size
            # greater than 3
            res += sum(dp[i].values())
        # to understand res - n https://www.youtube.com/watch?v=YIMwwT9JdIE
        return res - n

sol = Solution()
nums = [2,4,6,8,10]
nums = [7,7,7,7,7]
print(sol.numberOfArithmeticSlices(nums))