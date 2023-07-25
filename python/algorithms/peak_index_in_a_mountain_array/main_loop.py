#!/usr/bin/env python3

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        size = len(arr)
        if size == 3:
            return 1
        for i in range(1, size - 1):
            if arr[i] > arr[i+1]:
                return i