#!/usr/bin/env python

class Solution:
    def maxScore(self, s: str) -> int:
        zeros = [0] * (len(s) + 1)
        ones = [0] * (len(s) + 1)
        size = len(s)
        ans = 0

        for i in range(size):
            zeros[i]  = zeros[i - 1]
            ones[size -i -1] = ones[size - i]
            if s[i] == '0':
                zeros[i] = zeros[i-1] + 1
            if s[size - i - 1] == '1':
                ones[size -i -1] = ones[size - i] + 1
        ones[0] -= 1
        if s[-1] == '0':
            zeros[-2] -= 1
        for i in range(size):
            ans = max(zeros[i] + ones[i], ans)
        return ans