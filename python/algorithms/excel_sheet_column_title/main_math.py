#!/usr/bin/env python

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber < 27:
            return chr(64 + columnNumber)
        res = ""
        power = 0
        numb_ref = 0
        arr = []
        while (columnNumber > 26 ** (power)):
            numb_ref += 26 ** power
            power += 1
        power-=1
#        print(power)
        add = 0
        while power >= 0:
            tmp = columnNumber // (26 ** power)
            arr.append(tmp)
            columnNumber %= (26 ** power)
            power-=1
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] == 0:
                arr[i] = 26
                arr[i-1] -=1
            if arr[i] ==-1:
                arr[i] = 25
                arr[i-1] -= 1
        for i in arr:
            if i:
                res += chr(64 + i)
        return res

import sys
sol = Solution()
print(sol.convertToTitle(int(sys.argv[1])))