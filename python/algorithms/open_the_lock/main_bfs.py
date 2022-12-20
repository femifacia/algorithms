#!/usr/bin/env python3

from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if target == "0000":
            return 0
        if "0000" in deadends:
            return -1
        to_see = deque([("0000", 0)])
        visited = {}
        while (to_see):
            current, dist = to_see.pop()
            for i in range(4):
                for j in [-1, 1]:
                    upd = current[:i] + chr(ord('0') + ((ord(current[i]) - ord('0') + j) % 10)) + current[i+1:]
                    if upd not in visited and upd not in deadends:
                        if upd == target:
                            return dist + 1
                        to_see.appendleft((upd, dist + 1))
                        visited[upd] = 1
        return -1

sol = Solution()
deadends = ["8888"]
target = "0009"
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(sol.openLock(deadends, target))