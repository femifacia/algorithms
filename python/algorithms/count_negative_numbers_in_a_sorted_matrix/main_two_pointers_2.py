#!/usr/bin/env python3

#TC: O(n+m)
#SP: O(1)

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        if grid[-1][-1] >= 0:
            return 0
        ans = 0
        m = len(grid)
        n = len(grid[0])
        i = 0
        j = n - 1
        while (i < m and j >= 0):
            if grid[i][j] < 0:
                ans += (m - i)
                j-=1
            else:
                i+=1
        return ans
    
sol = Solution()
grid = [[3,2],[1,0]]
grid = [[4,3,-1,-1],[3,2,-1,-1],[1,1,-1,-2],[1,-1,-2,-3]]
[print(i) for i in grid]
print(sol.countNegatives(grid))
