#!/usr/bin/env python3

from collections import Counter
import numbers
import sys


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n = str(n)
        n = Counter(n)
#        print(n)
        for i in range(30):
            numb = str(1 << i)
            if n == Counter(numb):
                return  (True)
        return (False) 

sol = Solution()
print(sol.reorderedPowerOf2(int(sys.argv[1])))

