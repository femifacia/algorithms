#!/usr/bin/env python3

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return nums1.intersection(nums2)
    
sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersection(nums1, nums2))