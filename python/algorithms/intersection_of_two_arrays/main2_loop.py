#!/usr/bin/env python3

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
        return res
    
sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersection(nums1, nums2))