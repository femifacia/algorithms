#!/usr/bin/env python3

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        product = 1
        nb = 0
        while (n > 0):
            nb = n % 10
            summ += nb
            product *= nb
            n //= 10
        return product - summ