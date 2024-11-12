from typing import List
from collections import defaultdict
from bisect import bisect_left
from bisect import bisect_right
from heapq import heappush


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        dp = defaultdict(list)
        dp_2 = [float('inf')]
        dp_3 = {}
        index = []
        ans = []
        max_price = float('inf')
        for i,j in items:
            heappush(dp[i], -j)
            index.append(i)
            max_price = min(i, max_price)
        index.sort()
        for i in index:
            if dp[i][0] <= dp_2[-1]:
                dp_2.append(dp[i][0])
                dp_3[i] = dp[i][0]
            else:
                dp_2.append(dp_2[-1])
                dp_3[i] = dp_2[-1]
        for i in queries:
            idx = bisect_left(index, i)
            if idx >= len(index):
                idx -= 1
            if  i < max_price:
                #print(i, index[idx])
                ans.append(0)
                continue
            if index[idx] > i:
                idx -= 1

            ans.append(-dp_3[index[idx]])

        return ans
    

sol = Solution()
items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]


items = [[1,2],[1,2],[1,3],[1,4]]
queries = [1]

items = [[10,1000]]
queries = [5]
print(sol.maximumBeauty(items, queries))