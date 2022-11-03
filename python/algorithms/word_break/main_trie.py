#!/usr/bin/env python3

from collections import defaultdict
from string import ascii_letters

#dont pass all tests I will check if after

class TrieNode:
    def __init__(self) -> None:
        #each node has to know if it is a word or not
        self.isWord = False
        #each node has a dictionary which at a c char associate a TrieNode
        self.children = {}
        #children could have been init like this self.children = {c : None for c in ascii_letters}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #we start at the root
        current = self.root
        for i in word:
            if not i in current.children:
                #if a letter of the word we want to insert is not the children of the current node we create it
                current.children[i] = TrieNode()
            #we go to the next element
            current = current.children[i]
        #the isWord of the last element is set to True cause it is a word
        current.isWord = True

    def search(self, word: str) -> bool:
        #we start at the root
        current = self.root
        for i in word:
            #if we notice that a node has not as child a letter of the word we return False
            if not i in current.children:
                return False
            current = current.children[i]
        #if the last node of the word is not a Word, isWord would have been set to 0 otherwise 1
        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in prefix:
            if not i in current.children:
                return False
            current = current.children[i]
        return True

class Solution:

    def checkWordBreak(self, root : Trie, s : str) -> bool:
        size = len(s)
        if (size == 0):
            return True
        for i in range(1, size + 1):
            if (root.search(s[:i]) and self.checkWordBreak(root, s[i:])):
                return True
        return False

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        root = Trie()
        for word in wordDict:
            root.insert(word)
        return self.checkWordBreak(root, s)


sol =Solution()
s = "leetcode"
wordDict = ["leet","code"]
s = "applepenapple"
wordDict = ["apple","pen"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
s = "femiestfrais"
wordDict = ["femi", "fem", "ie", "stfraiss"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac"
s = "aaaaaaaaaaaaaaaaaaaaaac"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(sol.wordBreak(s, wordDict))