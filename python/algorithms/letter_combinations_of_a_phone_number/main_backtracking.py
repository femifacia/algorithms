#!/usr/bin/env python3

class Solution:

    def backtracking(self, word, level) -> None:
        if level == self.limit:
            self.ans.append(word)
            return
        for i in self.dict[self.digits[level]]:
            self.backtracking(word + i, level + 1)

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        self.ans = []
        self.digits = digits
        self.dict = {str(i+ 2):chr(97 + 3 * i) + chr(97 + 3 * i + 1) + chr(97 +3 * i + 2) for i in range(5)}
        self.dict['7'] = 'pqrs'
        self.dict['8'] = 'tuv'
        self.dict['9'] = 'wxyz'
        self.limit = len(digits)
        self.backtracking("", 0)
#        print(self.dict)
        return self.ans

sol = Solution()
digits = "23"
print(sol.letterCombinations(digits))