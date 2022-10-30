#!/usr/bin/env python3

from string import ascii_letters


class TrieNode:
    def __init__(self) -> None:
        self.isWord = False
        self.s = {c : None for c in ascii_letters} #or I could have used an default dict


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, T : TrieNode, string : str, i = 0 ):
        if (not T):
            T = TrieNode()
        if i == len(string):
            T.isWord = True
        else:
            T.s[string[i]] = self.add(T.s[string[i]], string, i + 1)
        return T

    def insert(self, word: str) -> None:
        self.root.s[word[0]] = self.add(self.root.s[word[0]], word, 1)
        pass

    def search(self, word: str) -> bool:
        #print(self.root.s)
        T = self.root.s[word[0]]
        i = 1
        size = len(word)
        while (i < size and T):
            T = T.s[word[i]]
            #print(i)
            i+=1
        if not T:
            #print('ha')
            return False
        if not T.isWord:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        T = self.root.s[prefix[0]]
        i = 1
        size = len(prefix)
        while (i < size and T):
            T = T.s[prefix[i]]
            #print(i)
            i+=1
        if not T:
            #print('ha')
            return False
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