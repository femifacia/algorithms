#!/usr/bin/env python3

from collections import deque
from collections import defaultdict

#it workssss but verry slow

#before using set for visited I used

#here I creat a graph with words and apply a bfs on it

class Solution:

    # return 1 if there is only a difference of 1 letter between two words
    # we can go to a word for other one only if they have a difference of 1 word
    # so this function will help me to know what words are "neighbors"  

    def isDiff1(self, word1 : str, word2 : str) -> int:
        count = 0
        for i in self.range_size_word:
            if word1[i] != word2[i]:
                count += 1
            if count > 1:
                return False
        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if not endWord in wordList:
            return 0
        to_see = deque([(beginWord, 1)])
        size_word = len(beginWord)
        # I got the range above to avoid call the function a lot 
        self.range_size_word = range(size_word)
        # since now, visited is declares as a set
        # a hash set is much faster than an array 
        # REMINDER !!! ONLY Use a set or a hash map for a visited variable
        visited = {beginWord}
        # The Graph itself
        graph = defaultdict(list)
        # I make connections between words
        # If words have one letter difference, i made them neighbors 
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if self.isDiff1(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        # if the beginword not in wordlist i search all neighbors of begin words
        # we dont need to add to words wich have 1 diff with beginWord, beginWOd itself as neighbor cause
        # we dont need to go back to begin word BE ALERT !!! 
        if beginWord not in wordList:
            for i in wordList:
                if self.isDiff1(i, beginWord):
                    graph[beginWord].append(i)
        # The BFS
        while (to_see):
            current, dist = to_see.pop()
            for neighbor in graph[current]:
                if neighbor == endWord:
                    return dist + 1
                if neighbor not in visited:
                    to_see.appendleft((neighbor, dist + 1))
                    visited.add(neighbor)
        return 0

sol = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
#beginWord = 'hot'
#endWord = 'dog'
#wordList = ["hot","dog","dot"]
print(sol.ladderLength(beginWord, endWord, wordList))