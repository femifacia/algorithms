#!/usr/bin/env python3

from collections import Counter
import numbers
import sys


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        #So here we sort the digits on the number.
        n = "".join(sorted(str(n)))
#        print(n)
        for i in range(30):
#            And for each power of 2 we check if the sorted str == to our number sorted
            numb = str(1 << i)
            if n == "".join(sorted(numb)):
                return  (True)
        return (False) 

sol = Solution()
print(sol.reorderedPowerOf2(int(sys.argv[1])))

