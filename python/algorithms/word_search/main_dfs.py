#!/usr/bin/env python3

class Solution:

    def dfs(self, board : list[list[str]], i : int, j : int, word : str) -> bool:
        if word == "":
            return (True)
        for i1, j1, in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j- 1)]:
            if 0 <= i1 < self.height and 0 <= j1 < self.width and not self.seen[i1][j1] and board[i1][j1] == word[0]:
                self.seen[i1][j1] = True
                if (self.dfs(board, i1, j1, word[1:])):
                    return True
        self.seen[i][j] = False
        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        self.height = len(board)
        self.width = len(board[0])
        self.seen = [[0] * self.width for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                if board[i][j] == word[0]:
                    self.seen[i][j] = True
                    if (self.dfs(board, i, j, word[1:])):
                        return True
        return (False)

sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
word = "AAAAAAAAAAAAAAB"
print(sol.exist(board, word))