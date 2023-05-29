#!/usr/bin/env python3

import sys

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = len(num) -1
        carry = 0
        while (i >= 0 and k > 0):
            tmp = carry + num[i] + (k % 10)
            carry = tmp // 10
            tmp %= 10
            num[i] = tmp
            i-=1
            k//=10
        while i >= 0:
            tmp = carry + num[i]
            carry = tmp // 10
            tmp %= 10
            num[i] = tmp
            i-=1
        while k > 0:
            tmp = carry + (k % 10)
            carry = tmp // 10
            tmp %= 10
            num = [tmp] + num
            k //=10
        if carry:
            num = [1] + num
        return num


sol = Solution()
num=[1,5,6]
k = int(sys.argv[1])
print(sol.addToArrayForm(num, k))