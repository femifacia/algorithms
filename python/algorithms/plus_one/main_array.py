#!/usr/bin/env python3

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        val = "".join(str(i) for i in digits)
        val = int(val)
        val += 1
        val = str(val)
        val = list(val)
        val = list(map(int, val))
        return (val)

sol = Solution()
arr = [1,2,3]

print(sol.plusOne(arr))