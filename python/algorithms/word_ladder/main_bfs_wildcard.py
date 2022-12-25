#!/usr/bin/env python3

from collections import deque
from collections import defaultdict


# A BEAST !!!!
# The Upgrade of alphabet bfs
#complexity O(n*m) with m size of the word; n number of words in wordlist

#instead of doing a permutation of all letter, i use *
# for example look at the word hok as begin word and wordlist = hak hik pok pik hko 
# instead of changing all letter of hok we can just do hok: *ok, h*k, ho*
# and we see that the transformation of hak (h*k), hik (h*k), pok(*ok) are corresponding to hok
# they are its neighor doing just 3 permutations.

# We transform all words to find their neighbor and then do a bfs 

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if not endWord in wordList:
            return 0
        to_see = deque([(beginWord, 1)])
        size_word = len(beginWord)
        range_size_word = range(size_word)
        # to increase the speed, i used a dictionary. Stop using array or list to visited
        #use instead, dictionary or set
        visited = {beginWord : 1}
        #h*a will have as values hoa, hia, hla for exemple
        patternDict = defaultdict(list)
        #all possibilities of words
        wordPossibilites = defaultdict(list)
#        wordList.appendd(beginWord)
        if beginWord not in wordList:
            wordList.append(beginWord)
        for word in wordList:
            for j in range_size_word:
                pattern = word[:j] + "*" +word[j + 1:]
                patternDict[pattern].append(word)
                wordPossibilites[word].append(pattern)
        # BFS hehe
        while (to_see):
            current, dist = to_see.pop()
            for pattern in wordPossibilites[current]:
                if not pattern in visited:
                    for word in patternDict[pattern]:
                        if word == endWord:
                            return dist + 1
                        if word not in visited:
                            to_see.appendleft((word, dist + 1))
                            visited[word] = 1
                visited[pattern] = 1
        return 0

sol = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "sand"
endWord = "acne"
#beginWord = 'hot'
#endWord = 'dog'
#wordList = ["hot","dog","dot"]
print(sol.ladderLength(beginWord, endWord, wordList))