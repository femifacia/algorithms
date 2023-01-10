#!/usr/bin/env python3

class Solution:

    def dfs(self, board : list[list[str]], i : int, j : int) -> None:
        self.visited[i][j] = 1
        for i1, j1 in [(i + 1, j), (i - 1,j), (i, j + 1), (i, j - 1)]:
            if 0 <= i1 < self.height and 0 <= j1 < self.width and self.visited[i1][j1] == 0 and board[i1][j1] == 'O':
                self.dfs(board, i1, j1)

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.width = len(board[0])
        self.height = len(board)
        self.visited = [[0] * self.width for i in range(self.height)]
        # All O's group starting by the edges will be counted as visited
        # After that first search, All O not marked as visited will be flipped

        for i in [0, self.height - 1]:
            for j in range(self.width):
                if board[i][j] == 'O' and not self.visited[i][j]:
                    self.dfs(board, i, j)
        for i in range(self.height):
            for j in [0, self.width - 1]:
                if board[i][j] == 'O' and not self.visited[i][j]:
                    self.dfs(board, i, j)
        for i in range(1, self.height):
            for j in range(1, self.width -1):
                if board[i][j] == 'O' and not self.visited[i][j]:
                    board[i][j] = 'X'

sol = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol.solve(board)
[print(i) for i in board]