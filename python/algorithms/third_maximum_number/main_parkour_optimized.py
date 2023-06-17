#!/usr/bin/env python3

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        max_one = float('-inf')
        max_two = max_one
        max_three = max_one
        for i in nums:
            if i > max_one:
                max_three = max_two
                max_two = max_one
                max_one = i
            elif i > max_two and i < max_one:
                max_three = max_two
                max_two = i
            elif i > max_three and i < max_two:
                max_three = i
        return max_three if max_three != float('-inf') else max_one

arr = [1,2,2,5,3,5]
sol = Solution()
print(sol.thirdMax(arr))