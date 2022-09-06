#!/usr/bin/env python3

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic = {}
        for i in nums:
            if dic.get(i, 0):
                return True
            dic[i] = 1
        return (False)