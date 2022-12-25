#!/usr/bin/env python3

from collections import deque

#complecity O(n * m * z) with n = len(wordLIst), m = size of a word,  z= 26 (alphabet size)

#I test all combination of a word with 1 letter difference until find a word corresponding to endword

#doing it using dfs ensure me to find the word with the closest number of transformation

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if not endWord in wordList:
            return 0
        to_see = deque([(beginWord, 1)])
        size_word = len(beginWord)
        # I transform wordList into a set for better performances
        wordList = set(wordList)
        range_size_word = range(size_word)
        alphabet = [chr(97 + a) for a in range(26)]
        visited = {beginWord}
        while (to_see):
            current, dist = to_see.pop()
            for i in range_size_word:
                left = current[:i]
                right = current[i+1:]
                for a in alphabet:
                    word = left + a + right
                    if word in wordList and not word in visited:
                        if word == endWord:
                            return dist + 1
                        to_see.appendleft((word, dist + 1))
                        visited.add(word)
        return 0

sol = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "sand"
endWord = "acne"
print(sol.ladderLength(beginWord, endWord, wordList))