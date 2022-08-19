from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        for i in range(n):
            board = ['.'*n for _ in range(n)]
            l = list(board[0])
            l[i] = 'Q'
            board[0] = ''.join(l)
            self.solveNQueensRec(board, n - 1, 0, i, ans)

        return ans

    def overlaps(self, board: List[str], i: int, j: int) -> bool:
        n = len(board)

        # check vertical
        q_count = 0
        for k in range(i + 1):
            if board[k][j] == 'Q':
                q_count += 1
        
        if q_count > 1:
            return True

        # check diagonal
        q_count = 1 if board[i][j] == 'Q' else 0
        diff = 1
        while True:
            top_right_i = i - diff
            top_right_j = j + diff

            # bottom_right_i = i + diff
            # bottom_right_j = j + diff

            top_left_i = i - diff
            top_left_j = j - diff

            # bottom_left_i = i + diff
            # bottom_left_j = j - diff

            has_top_right_neighbor = False

            if top_right_i >= 0 and top_right_j < n:
                has_top_right_neighbor = True
                if board[top_right_i][top_right_j] == 'Q':
                    q_count += 1

            # has_bottom_right_neighbor = False
            # if bottom_right_i < n and bottom_right_j < n:
            #     has_bottom_right_neighbor = True
            #     if board[bottom_right_i][bottom_right_j] == 'Q':
            #         q_count += 1

            has_top_left_neighbor = False
            if top_left_i >= 0 and top_left_j >= 0:
                has_top_left_neighbor = True
                if board[top_left_i][top_left_j] == 'Q':
                    q_count += 1

            # has_bottom_left_neighbor = False
            # if bottom_left_i < n and bottom_left_j >= 0:
            #     has_bottom_left_neighbor = True
            #     if board[bottom_left_i][bottom_left_j] == 'Q':
            #         q_count += 1

            if not has_top_right_neighbor and not has_top_left_neighbor:
                break

            diff += 1
        
        if q_count > 1:
            return True

        return False

    def solveNQueensRec(self, board: List[str], n: int, i: int, j: int, ans: List[List[str]]):
        if self.overlaps(board, i, j):
            return False
        
        if n == 0:
            ans.append(board)
            return True

        for c in range(len(board)):
            if (i + 1) < len(board):
                new_board = board.copy()
                old_row_string = new_board[i + 1]
                new_row_list = list(old_row_string)
                new_row_list[c] = 'Q'
                new_board[i + 1] = ''.join(new_row_list)
                
                if not self.solveNQueensRec(new_board, n - 1, i + 1, c, ans):
                    new_board[i] = old_row_string
            
        return False


sol = Solution()
# print(sol.overlaps(['.Q...', '...Q.', 'Q....', '....Q', '..Q..'], 4, 2))
print(sol.solveNQueens(4))


