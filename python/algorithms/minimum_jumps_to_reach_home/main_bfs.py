#!/usr/bin/env python3

from collections import deque

class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        size = 6000
        if (x == 0):
            return 0
        to_see = deque([([0],0,0)])
        seen = [0] * (size)
        seen[0] = 1
        for i in forbidden:
            seen[i] = 1
        print(seen)
        while (to_see):
            current, direction, jump = to_see.pop()
#            print(current)
#            if (current == a):
#                return jump
            for i,j in [(current[-1] + a, direction + 1), (current[-1] - b, direction - 1)]:
                if i >= 0 and j >= 0 and i < size and seen[i] == 0:
                    if i == x:
                        print("sahhh", current)
                        return jump + 1
                    seen[i] = 1
                    to_see.appendleft((current + [i],j,jump+ 1))
        return -1

sol = Solution()
a = 806
b = 1994
x = 326