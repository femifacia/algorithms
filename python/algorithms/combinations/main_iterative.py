#!/usr/bin/env python3

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        comb = list(range(1, k + 1))
        res.append(comb[:])
        
        while True:
            for i in reversed(range(k)):
                max_at_i = n - k + 1 + i
                #max_at_i the the maximum we can have at a position i
                #so we start from the right to find the rightest element which need augmentation
                #if we don't find it (if the if don't trigger) the else will be called and it will be the
                #end of our program
#                print("i =", i, "zarbi =", n - k + 1 + i)
                if comb[i] != max_at_i:
                    break
            else:
                break
#            print("before", comb)
#if we are here , it means the previous else didn't trigger.
# so we increment comb[i] by one and adjusting all values after it

#Yes it is pretty tricky  you are right but that is the iterative way to do this without using recursion
            comb[i] += 1
            for j in range(i + 1, k):
                comb[j] = comb[j - 1] + 1
#            print("after", comb)
            res.append(comb[:])
        
        return res

sol = Solution()
print(sol.combine(4, 3))