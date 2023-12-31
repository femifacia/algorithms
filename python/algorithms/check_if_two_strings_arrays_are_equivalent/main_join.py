#!/usr/bin/env python

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(i for i in word1) == "".join(i for i in word2)