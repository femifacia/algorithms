#!/usr/bin/env python3
import sys


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        size1 = len(a)
        size2 = len(b)
        ret = 0
        if (size1 > size2):
            b = ("0" * (size1-size2)) + b
            size2 = size1
        elif (size2 > size1):
            a = ("0" * (size2-size1)) + a
            size1 = size2
#        print("a", a)
#        print("b", b)
        size1 -= 1
        while (size1 >= 0):
            unit = ord(a[size1]) + ord(b[size1]) - 2 * ord('0') + ret
            ret = 0 if ret == 0 else ret - 1
            if (unit >= 2):
                ret += 1
                unit %= 2            
            res = str(unit) + res
            size1 -=1
        if (ret):
            res = str(ret) + res
        return (res)

sol = Solution()

print(sol.addBinary(sys.argv[1], sys.argv[2]))