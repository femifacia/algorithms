#!/usr/bin/env python3

import sys

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sign = 1
        if num1[0] == '-':
            num1 = num1[1:]
            sign *= -1
        if num2[0] == '-':
            num2 = num2[1:]
            sign *= -1
        arr = []
        res = 0
        zero_val = ord('0')
        index = 0
        tour = 0
        for x in num1[::-1]:
            res = 0
            index  = tour
            carry = 0
            for y in num2[::-1]:
                tmp = ((ord(y) - zero_val) * (ord(x) - zero_val)) + carry
                carry = tmp // 10
                res += ((tmp % 10) * 10 ** index)
                index += 1
            if carry:
                res += (carry * (10 ** index))
            arr.append(res)
#            print(arr)
            tour += 1
        res = sum(arr) * sign

        return str(res)

sol = Solution()
print(sol.multiply(sys.argv[1], sys.argv[2]))