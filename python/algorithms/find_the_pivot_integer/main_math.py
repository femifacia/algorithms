#!/usr/bin/env python3

class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 1
        left_sum = 1
        right = (n*(n+1))/2
        while left <= n:
            if left_sum == right:
                return left
            right -= left
            left += 1
            left_sum += left
        return -1