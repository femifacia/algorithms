#!/usr/bin/env python3

from  collections import deque

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        size = len(arr)
        seen = [0] * size
        to_see = [start]
        seen[start] = 1
        while (to_see):
            current = to_see.pop()
            print(current)
            if (arr[current] == 0):
                return True
            for i in [current + arr[current], current - arr[current]]:
                if i >= 0 and i < size and not seen[i]:
                    seen[i] = 1
                    to_see.append(i)
        return False

sol = Solution()
arr = [4,2,3,0,3,1,2]
start = 5
print(sol.canReach(arr, start))