#!/usr/bin/env python

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        #ans = [1] * (rowIndex + 1)

        #return ans
        if rowIndex == 0:
            return [1]
        old = [1]
        tmp = [1,1]
        for i in range(2, rowIndex + 1):
            tmp.append(1)
            for j in range(1, len(tmp) - 1):
                tmp[j] = old[j] + old[j-1]
            old = tmp
        return tmp
