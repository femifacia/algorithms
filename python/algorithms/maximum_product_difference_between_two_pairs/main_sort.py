#!/usr/bin/env python

# We can also make another solution in `O(1)` time by using
# 4 variables; two to he biggest numbers and other two for lowest elements 
# and do the diff later but I won’t implement this.

# Some ifs will do the job ;)

class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])