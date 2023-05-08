#!/usr/bin/env python3

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = [set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]
        res = []

        for word in words:
            word_set = set(word.lower())
            for row in rows:
                if (row & word_set) == word_set:
                    res.append(word)
                    break
        return res
