#!/usr/bin/env python3

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_dic = {order[i] : i for i in range(len(order))}
        #print(order_dic)
        size = len(words)
        j = 0
        while (size != 1):
            i = 0
            while i + 1< size:
                if (j >= len(words[i])):
                    if i != 0:
                        return False
                    del words[i]
                    size -= 1
                    continue
                if (j >= len(words[i + 1])):
                    return False
                if (order_dic[words[i][j]] > order_dic[words[i + 1][j]]):
                    return False
                if (order_dic[words[i][j]] < order_dic[words[i + 1][j]]):
                    size-=1
                    del words[i]
                    continue
                i += 1
            j += 1
        return True

sol = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
words = ["apple","apple", "m", "aa"]
order = "abcdefghijklmnopqrstuvwxyz"
print(sol.isAlienSorted(words, order))