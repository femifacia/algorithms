#!/usr/bin/env python

from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first_min_price = float("inf")
        second_min_price = float("inf")
        for i in prices:
            if i <  first_min_price:
                first_min_price, second_min_price = i, first_min_price
            elif i < second_min_price:
                second_min_price = i
        return money if second_min_price + first_min_price > money else money - first_min_price - second_min_price