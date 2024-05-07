#!/usr/bin/env python

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        i = 0
        j = len(s) - 1
        set1 = 0
        set2 = 0
        while i <= j:
            if s[i] in vowels:
                set1 += 1
            if s[j] in vowels:
                set2 += 1
            i+=1
            j-=1
        return set1 == set2