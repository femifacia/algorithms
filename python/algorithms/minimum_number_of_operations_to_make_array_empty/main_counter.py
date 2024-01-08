#!/usr/bin/env python

from collections import Counter
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        remain = len(nums)
        for i in count:
            if count[i] == 1:
                return -1
            if count[i] % 3 ==0:
                ans += 1
                count[i] -= 3
                remain -= 3
            elif count[i] % 2 == 0:
                ans += 1
                count[i] -= 2
                remain -= 2
        while remain > 0:
            for i in count:
                if count[i] == 1:
                    return -1
                if count[i] and count[i] % 3 ==0:
                    ans += 1
                    count[i] -= 3
                    remain -= 3
                elif count[i] and count[i] % 2 == 0:
                    ans += 1
                    count[i] -= 2
                    remain -= 2
                elif count[i]:
                    ans += 1
                    count[i] -= 3
                    remain -= 3

        return ans