#!/usr/bin/env python3

from collections import defaultdict
from string import ascii_letters

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