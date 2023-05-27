#!/usr/bin/env python3

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        seen = set()
        retired = set()
        res = 0
        for i in nums:
            if i in seen:
                if not i in retired:
                    res -= i
                    retired.add(i)
            else:
                res += i
                seen.add(i)
        return res