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
        left_height = right_height= m -1
        width = n -1
        while (width  - 1>= 0 and grid[right_height][width - 1] < 0):
            width -= 1
        while left_height - 1 >= 0 and grid[left_height - 1][-1] < 0:
            left_height -= 1
        while (right_height > 0 and right_height != left_height and grid[right_height][width] < 0):
            if right_height - 1 >= 0 and grid[right_height -1][width] >= 0:
                width += 1
                ans += (m - right_height)
            else:
                right_height -= 1
        ans += ((n - width) * (m - right_height ))
        return ans
    
sol = Solution()
grid = [[3,2],[1,0]]
grid = [[4,3,-1,-1],[3,2,-1,-1],[1,1,-1,-2],[1,-1,-2,-3]]
[print(i) for i in grid]
print(sol.countNegatives(grid))
