#!/usr/bin/env python3

from collections import defaultdict
from string import ascii_letters

class TrieNode:
    def __init__(self) -> None:
        self.isWord = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for i in word:
            if not i in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.isWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for i in word:
            if not i in current.children:
                return False
            current = current.children[i]
        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in prefix:
            if not i in current.children:
                return False
            current = current.children[i]
        return True


# Your Trie object will be instantiated and called as such:
word = ["app", "apple"]
word_to_search = ["kl", "jean", "femi", "ap", "a", "app", "apple"]
start_with = ["ji", "fe", "femi", "c", "cesc"]
obj = Trie()
for i in word:
    obj.insert(i)
for i in word_to_search:
    print(i, "  ", end="")
    print(obj.search(i))
for i in start_with:
    print("prefix", i, " ", end="")
    print(obj.startsWith(i))
#param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)