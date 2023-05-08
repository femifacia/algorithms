#!/usr/bin/env python3

arr = [5,4,9,10]
#      0  1 2 3
sah = {5,4,9,10,"femi"}
femi = 102 * 1 + 101 * 2 + chr('m') * 3 + chr('i') * 4
femi = 504


class Solution:

    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        nums1 = set(nums1)
        for i in nums1:
            if i in nums2:
                res.append(i)
        return res
    
sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersection(nums1, nums2))