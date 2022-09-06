#!/usr/bin/env python3

from cmath import log10
from math import log

#dont work in python
#look at c version

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        float_result = float((log(n) / log(3)))
        integer_result = int(((log(n) / log(3))))
        return (n != 0) and float_result == integer_result

sol = Solution()
print(sol.isPowerOfThree(243))