#!/usr/bin/env python3

import sys
from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(num)
        for i in range(len(num)):
            if count[str(i)] != int(num[i]):
                return False
        return True

sol = Solution()
print(sol.digitCount(sys.argv[1]))