#!/usr/bin/env python3

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max( i.count(" ") + 1 for i in sentences)