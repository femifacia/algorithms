#!/usr/bin/env python

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        power = len(columnTitle) -1
        res = 0
        for i in columnTitle:
            res += (26 ** power  * (ord(i) - 64))
            power -= 1
        return res