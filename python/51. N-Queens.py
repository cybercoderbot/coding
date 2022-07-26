"""
51. N-Queens
Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
"""


class Solution:
    def solveNQueens(self, N: int) -> List[List[str]]:
        """
        Recursive backtracking row-by-row to populate res.
        """

        board = [["."]*N for _ in range(N)]

        def backtrack(i, seen):
            """Recursively populate the n queens via backtracking."""
            if i == N:
                return res.append(["".join(x) for x in board])

            for j in range(N):
                pos = {("col", j), ("diag", i-j), ("anti", i+j)}
                if not pos & seen:
                    board[i][j] = "Q"
                    seen |= pos
                    backtrack(i+1, seen)
                    board[i][j] = "."
                    seen -= pos

        res = []
        seen = set()
        backtrack(0, seen)
        return res
