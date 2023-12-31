#!/usr/bin/env python

from collections import Counter
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        string = ''.join(i for i in words)
        count = Counter(string)
        size = len(words)
        for i in count:
            if count[i] % size:
                return False
        return True
