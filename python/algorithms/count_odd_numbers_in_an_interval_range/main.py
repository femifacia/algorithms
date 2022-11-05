#!/usr/bin/env python3

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (low == high):
            return low % 2 != 0
        nbr = (high - low - 1) // 2
        is_low_odd = (low % 2 != 0)
        return  is_low_odd + (high % 2 != 0) + (nbr if is_low_odd else high - nbr)


class Other:
    def countOdds(self, low, high):
        return (high + 1) / 2 - low / 2