#!/usr/bin/env python3

import math
class Solution:
    def mySqrt(self, x: int) -> int:
        n=x
        if x<2:
            return x
        for i in range(int(math.log(n,2))+1):
            n=(n+(x/n))/2
        return int(n)