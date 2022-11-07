#!/usr/bin/env python3

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return (max(sum(i) for i in accounts))
