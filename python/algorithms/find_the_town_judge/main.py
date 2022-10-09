#!/usr/bin/env python3

from collections import Counter


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trusted_people = [0] * n
        people_who_trust = [0] * n
        for person, trusted in trust:
            trusted_people[trusted - 1] += 1
            people_who_trust[person -1] = 1
        if not 0 in people_who_trust:
            return -1
        idx = people_who_trust.index(0)
        if trusted_people[idx] != n -1:
            return -1
        return idx + 1


sol = Solution()
n = 3
trust = [[1,3],[2,3],[3,1]]
n = 3
trust = [[1,3],[2,3]]
n = 2
trust = [[1,2]]
print(sol.findJudge(n , trust))