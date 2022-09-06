#!/usr/bin/env python3

class Solution:

    def time_boss(self, target, informTime, highest_time):
        if (target == []):
            return(0, highest_time)
        temp = max(informTime[i] for i in target)
        if (len(target) == 1 and highest_time == 0):
            return(temp, 0)
        highest_time -= temp
        if (highest_time <= 0):
            highest_time *= -1# temp
            print(temp)
            return (temp, highest_time)
        return (0, highest_time)

    def get_subordonates(self, target, boss):
        sub = []
        for i in target:
            sub += boss[i]
        return (sub)

    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        temp = 0
        boss = [[] for i in range(n)]
        for i in range(n):
            if (i == headID):
                continue
            boss[manager[i]].append(i)
        target = [headID]
        print(boss)
        highest_time = 0
        for i in range(len(boss)):
    #        print("before", target, headID)
            tmp, highest_time = self.time_boss(target, informTime, highest_time)
            temp += tmp
            target = self.get_subordonates(target, boss)
            print("after", target)
        return (temp)

sol = Solution()
print(sol.numOfMinutes(12, 2,[6,5,-1,2,10,0,10,3,4,7,2,5],[589,0,472,232,237,775,386,890,0,0,940,0]))
#print(sol.numOfMinutes(11, 4,[5,9,6,10,-1,8,9,1,9,3,4], [0,213,0,253,686,170,975,0,261,309,337]))
