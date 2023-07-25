#!/usr/bin/env python3

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        size = len(arr)
        if size == 3:
            return 1
        left = 0
        right = size
        while left < right:
            mid = (left + right) // 2
 #           print(mid,left,right)
            if arr[mid - 1] > arr[mid]:
                right = mid - 1
            elif arr[mid + 1] > arr[mid]:
                left = mid + 1
            else:
                return mid
#        print(left, right, mid)
        return max((arr[left], left),(arr[mid + 1],mid + 1))[1]

sol = Solution()
arr = [1,3,29,30,34,35,42,60,64,73,91,94,91,85,80,75,71,63,54,53,42,27,24,21,14,11,10,9]
arr = [0,10,5,2]
arr = [0,2,1,0]
print(sol.peakIndexInMountainArray(arr))
print(arr[sol.peakIndexInMountainArray(arr)])