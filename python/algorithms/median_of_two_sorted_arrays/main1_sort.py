#!/usr/bin/env python3

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sorted_arr = []
        for i in nums1 + nums2:
            sorted_arr.append(i)
        sorted_arr.sort()
        size = len(sorted_arr)
        return sorted_arr[size // 2] if size % 2 != 0 else (sorted_arr[size // 2] + sorted_arr[size // 2 - 1]) / 2