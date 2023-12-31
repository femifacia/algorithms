#!/usr/bin/env python

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        size = len(arr)
        quarter = size // 4
        for i in range(size - quarter):
            if arr[i] == arr[i + quarter]:
                return arr[i]