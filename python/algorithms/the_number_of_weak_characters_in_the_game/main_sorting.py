#!/usr/bin/env python3

import math


class Solution:

    def isWeakCharacter(self, power : int, power_dic : dict, elm : list[int],pos : int, weak) ->int:
        for j in power_dic:
            if j > power or j < power:
                for x, y in power_dic[j]:
                    if x > elm[0] and y > elm[1]:
#                        weak[(elm[0], elm[1])] = 1
                        return 1
                    elif x < elm[0] and y < elm[1]:
                        print("p", elm, x, y)
                        weak[(x,y)] = 1
        return (0)

    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        nbr = 0
        print(properties)
        print(sorted(properties))
        #properties = sorted(properties)
        max_until_now = -math.inf
        properties.sort(key=lambda x: (-x[0], x[1]))
        print(properties)
        for i in properties:
            if max_until_now > i[1]:
                nbr+=1
            else:
                max_until_now = i[1]
#        print(weak, nbr)
        return nbr

sol = Solution()
properties = [[2,2],[3,3]]
properties = [[5,5],[6,3],[3,6]]
properties = [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]
print(sol.numberOfWeakCharacters(properties))