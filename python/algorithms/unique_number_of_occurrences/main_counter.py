#!/usr/bin/env python3

from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = Counter(arr)
        vals = list(count[i] for i in count)
        return len(set(vals)) == len(vals)