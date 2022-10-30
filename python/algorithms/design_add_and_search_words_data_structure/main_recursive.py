#!/usr/bin/env python3

class TrieNode:
    def __init__(self) -> None:
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.word_inside = {}
        self.max_len = 0

    def addWord(self, word: str) -> None:
        current = self.root
        if word in self.word_inside:
            return
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.isWord = True
        self.max_len = max(len(word), self.max_len)

    def dfs(self, root : TrieNode, word : str, i : int) -> bool:
        if i == len(word):
            return root.isWord
        if not root:
            return False
        if (word[i] == '.'):
            for c in root.children.keys():
                if (self.dfs(root.children[c], word, i+ 1)):
                    return True
            return False
        else:
            if word[i] not in root.children:
                return False
            return self.dfs(root.children[word[i]], word, i+ 1)
    
    
    def search(self, word: str) -> bool:
        if word in self.word_inside:
            return True
        if len(word) > self.max_len:
            return False
        res = (self.dfs(self.root, word, 0))# == True
        if (res):
            self.word_inside[word] = 1
        return res

word = ["app", "apple", "bad", "baaal"]
word_to_search = ["kl", "jean", "femi", "ap", ".a..", "ap.", "ap.e"]
start_with = ["ji", "fe", "femi", "c", "cesc"]
obj = WordDictionary()
for i in word:
    obj.addWord(i)
    print("added", i)
print("")
for i in word_to_search:
    print(i, "  ", end="")
    print(obj.search(i))


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)