#!/usr/bin/env python3

from bisect import bisect_right

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        index = bisect_right(letters, target)
        if index != len(letters):
            return letters[index]
        return letters[0]