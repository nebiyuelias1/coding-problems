from typing import List


class Solution:
    def existsRec(self, board: List[List[str]], word: str, i: int, j: int, visited: List[List[bool]]) -> bool:
        if len(word) == 0:
            return True

        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
            return False

        if visited[i][j]:
            return False

        if board[i][j] == word[0]:
            visited[i][j] = True
            if (self.existsRec(board, word[1:], i - 1, j, visited)
                or self.existsRec(board, word[1:], i + 1, j, visited)
                or self.existsRec(board, word[1:], i, j + 1, visited)
                    or self.existsRec(board, word[1:], i, j - 1, visited)):
                return True
            else:
                visited[i][j] = False

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        explored_board = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.existsRec(board, word, i, j, explored_board):
                    return True

        return False


board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], [
    "A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
word = "AAAAAAAAAAAAAAB"

sol = Solution()
print(sol.exist(board, word))
