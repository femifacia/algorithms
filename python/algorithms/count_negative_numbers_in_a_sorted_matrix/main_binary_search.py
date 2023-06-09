#!/usr/bin/env python3

#TC: O(mlog(n))
#SP: O(1)

import bisect

class Solution:

    def binarySearch(self,line : list[int], target : int, size : int) -> int:
        left = 0
        right = size

        while left < right:
            mid  = (left + right) // 2
#            print(line,mid,left,right)
            if line[mid] > target:
                left = mid + 1
            elif line[mid] < target:
                right = mid
            else:
                while mid < size and line[mid] == target:
                    mid += 1
                return mid
        return left

    def countNegatives(self, grid: list[list[int]]) -> int:
        if grid[-1][-1] >= 0:
            return 0
        ans = 0
        n = len(grid[0])
        for i in grid:
            index = self.binarySearch(i,0,n)
            ans += (n - index)
        return ans
    
sol = Solution()
grid = [[4,3,0,0,-1],[3,2,-1,-1,-1],[1,1,-1,-2,-2],[1,-1,-2,-3,-3]]
grid = [[3,2],[1,0]]
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid = [[3,2],[-3,-3],[-3,-3],[-3,-3]]
[print(i) for i in grid]
print(sol.countNegatives(grid))
