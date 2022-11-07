#!/usr/bin/env python3

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

    def isAlienSorted2(self, words, order):
        return words == sorted(words, key=lambda w: map(order.index, w))


sol = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
words = ["apple","apple", "m", "aa"]
order = "abcdefghijklmnopqrstuvwxyz"
print(sol.isAlienSorted(words, order))