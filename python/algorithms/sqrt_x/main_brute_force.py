#!/usr/bin/env python3

class Solution:
    def mySqrt(self, x: int) -> int:
        nbr = 0
        while nbr * nbr < x:
            nbr += 1
        return nbr if nbr * nbr == x else nbr - 1