#!/usr/bin/env python3

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        return max((arr[i],i)for i in range(len(arr)))[1]