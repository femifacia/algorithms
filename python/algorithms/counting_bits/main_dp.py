#!/usr/bin/env python3

class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [1] * (n + 1)
        dp[0] = 0
        for i in range(2 , n + 1):
            #even nombers are composed by the sum of their half
            #for exemple 6 is 3 + 3.
            # 3 is 11 + 11
            #  when you have to add the same number two times, the number of 1 dont change
            # so as you see, 11 + 11 is  110
            # so the number of 1 is the same than the half 
            if i % 2 == 0:
                dp[i] = dp[i//2]
            #odd numers are the sum of their half + 1
            # ex 7 == 3 + 3 + 1
            # so the number of 1 bits of 3 + 3 is the number of bits of 3 and we add 1
            else:
                dp[i] = dp[i//2] + 1
        return dp

sol = Solution()
n = 2
print(sol.countBits(n))