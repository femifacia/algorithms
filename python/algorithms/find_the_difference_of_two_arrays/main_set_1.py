#!/usr/bin/env python3

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        ans1 = []
        ans2 = []

        for i in nums1:
            if i not in nums2:
                ans1.add(i)
        for i in nums2:
            if i not in nums1:
                ans2.add(i)
        return [ans1, ans2]