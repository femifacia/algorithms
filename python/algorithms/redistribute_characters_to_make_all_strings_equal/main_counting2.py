#!/usr/bin/env python


from collections import Counter
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = {}
        for i in words:
            for j in i:
                count[j] = count.get(j, 0) + 1
        size = len(words)
        for i in count:
            if count[i] % size:
                return False
        return True
