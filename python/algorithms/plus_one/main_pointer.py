#!/usr/bin/env python3

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # we could have called ret carry cause carry is "retenue" in french
        ret = 1
        index = len(digits) - 1
        while (index >= 0):
            digits[index] += ret
            if digits[index] >= 10:
                ret = 1
                digits[index] = 0
            else:
                ret = 0
            index -= 1
            if (ret == 0):
                break
        if ret:
            digits = [1] + digits
        return digits

sol = Solution()
arr = [9]

print(sol.plusOne(arr))