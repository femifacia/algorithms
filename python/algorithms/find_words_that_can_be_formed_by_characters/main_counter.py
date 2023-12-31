#!/usr/bin/env python

from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_chars = Counter(chars)
        ans = 0
        for i in words:
            tmp = Counter(i)
            for j in tmp:
                if not j in count_chars or tmp[j] > count_chars[j]:
                    ans-=len(i)
                    break
            ans += len(i)
        return ans