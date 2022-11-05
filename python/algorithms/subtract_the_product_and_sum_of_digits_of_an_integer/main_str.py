#!/usr/bin/env python3

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        product = 1
        for i in str(n):
            nb = int(i)
            summ += nb
            product *= nb
        return product - summ
