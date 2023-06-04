#!/usr/bin/env python3

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        ans1 = list(nums1 ^ (nums1 & nums2))
        ans2 = list(nums2 ^ (nums1 & nums2))

        return [ans1, ans2]