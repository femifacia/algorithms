#!/usr/bin/env python3

import sys

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        size = len(s)
        arr = []
        mul = 1
        power = 0
        res = 0
        while i < size and s[i] == ' ':
            i+=1
        if (i < size and s[i] == '-'):
            mul = -1
            i+= 1
        elif (i < size and s[i] == '+'):
            i+=1
        while (i < size and i == '0'):
            i+=1
        while (i < size and s[i] <= '9' and s[i] >= '0'):
            arr.append(s[i])
            i+=1
        arr = arr[::-1]
        for i in arr:
            res += ((int(i)) * (10 ** power))
            power += 1
        res *= mul
        if (res> 2**31 - 1):
            return (2**31 - 1)
        if (res < -(2 ** 31)):
            return (-(2**31))
        return (res)

sol = Solution()
print(sys.argv[1])
print(sol.myAtoi(sys.argv[1]))
