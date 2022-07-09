#!/usr/bin/env python3

class Solution:

    def decompGraph(self, parentId, children, informTime):
        arr = []
        if (parentId not in children):
            return ([informTime[parentId]])
        for i in children[parentId]:
            arr += self.decompGraph(i, children, informTime)
        for i in range(len(arr)):
            arr[i] = arr[i] +  informTime[parentId]
#        arr = list(map(lambda x: x + informTime[parentId], arr))
        #print("arr", arr)


        return (arr)

    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        #temp = 0
        boss = {}
        for i in range(n):
            if (i == headID):
                continue
            if manager[i] in boss:
                boss[manager[i]].append(i)
            else:
                boss[manager[i]] = [i]
        #target = [headID]
        #print("graph", self.decompGraph(headID, boss, informTime))
        #print(boss)
        return max(self.decompGraph(headID, boss, informTime))

sol = Solution()

print(sol.numOfMinutes(6, 2,[2,2,-1,2,2,2],[0,0,1,0,0,0]))
print(sol.numOfMinutes(1, 0,[-1],[0]))
print(sol.numOfMinutes(12, 2,[6,5,-1,2,10,0,10,3,4,7,2,5],[589,0,472,232,237,775,386,890,0,0,940,0]))
#print(sol.numOfMinutes(11, 4,[5,9,6,10,-1,8,9,1,9,3,4], [0,213,0,253,686,170,975,0,261,309,337]))
