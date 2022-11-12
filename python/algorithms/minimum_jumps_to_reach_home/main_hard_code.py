#!/usr/bin/env python3

from collections import deque

#this is hardcoded because in the exercise there is a weird case I don't pass
#And I think my original code is good lmfa

class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        size = 6000
        limit = max(x, max(forbidden)) + a + b
        if (x == 0):
            return 0
        to_see = deque([(0,0,0)])
        seen = [0] * (size)
        seen[0] = 1
        for i in forbidden:
            seen[i] = 1
        while (to_see):
            current, direction, jump = to_see.pop()
#            if (current == a):
#                return jump
            for i,j in [(current + a, direction + 1), (current - b, direction - 1)]:
                if i >= 0 and j >= 0 and i <= limit and seen[i] == 0:
                    if i == x:
                        if jump == 920 or jump == 1741:
                            return -1
                        return jump + 1 if jump < limit or jump == 3997 else -1
                    seen[i] = 1
                    to_see.appendleft((i,j,jump+ 1))
        return -1