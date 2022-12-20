#!/usr/bin/env python3

from collections import deque

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        visited = {(0,0) : 1}
        to_see = deque([(0,0)])
        while (to_see):
            vol1, vol2 = to_see.pop()
            #print(vol1, vol2)
            if vol1 <= jug1Capacity:
                new_vol = min(jug1Capacity, vol1 + vol2)
                for new_vol1, new_vol2 in [(new_vol, max(0, vol2 - (new_vol - vol1 ))), (jug1Capacity, vol2), (0, vol2)]:
                    if (new_vol1, new_vol2) not in visited:
                        if new_vol1 + new_vol2 == targetCapacity:
                            return True
                        to_see.appendleft((new_vol1, new_vol2))
                        visited[(new_vol1, new_vol2)] = 1

            if vol2 <= jug2Capacity:
                new_vol2 = min(jug2Capacity, vol1 + vol2)
                new_vol1 = max(0, vol1 - (new_vol2 - vol2 ))
                for new_vol1, new_vol2 in [(new_vol1, new_vol2), (vol1, jug2Capacity), (vol1,0)]:
                   if (new_vol1, new_vol2) not in visited:
                        if new_vol1 + new_vol2 == targetCapacity:
                            return True
                        to_see.appendleft((new_vol1, new_vol2))
                        visited[(new_vol1, new_vol2)] = 1
#                new_vol2 = jug2Capacity
#                new_vol1 = vol1
#                if (new_vol1, new_vol2) not in visited:
#                    to_see.appendleft((new_vol1, new_vol2))
#                    visited[(new_vol1, new_vol2)] = 1
            

        return False

sol = Solution()
jug1Capacity = 3
jug2Capacity = 5
targetCapacity = 4
jug1Capacity = 5
jug2Capacity = 7
targetCapacity = 8
print(sol.canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))