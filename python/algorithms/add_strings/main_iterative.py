#!/usr/bin/env python3

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        zero = ord('0')
        while (i >= 0 and j >= 0):
            tmp = ord(num1[i]) + ord(num2[j]) - (zero + zero) + carry
            carry = tmp // 10
            tmp %= 10
            res = str(tmp) + res
            i-=1
            j-=1
        if j >= 0:
            num1,i = num2,j
        while i >= 0:
            tmp = ord(num1[i]) - zero + carry
            carry = tmp // 10
            tmp %= 10
            res = str(tmp) + res
            i-=1
        if carry:
            res = '1' + res
        return res