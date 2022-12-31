#!/usr/bin/env python3

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    nbr = 6
    if num == nbr:
        return 0
    if num > nbr:
        return -1
    return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while (left < right):
            middle = (left + right) // 2
            res = guess(middle)
            if (res == 0):
                return middle
            elif res > 0:
                left = middle + 1
            else:
                right = middle
        return left

sol = Solution()
print(sol.guessNumber(10))