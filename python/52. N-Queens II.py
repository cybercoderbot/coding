"""
52. N-Queens II
Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1
"""


class Solution:
    def totalNQueens(self, N: int, diag1=set(), diag2=set(), cols=set(), r=0) -> int:
        """
        Backtracking
        """
        if r == N:
            return 1

        res = 0
        for c in range(N):
            if r+c in diag1 or r-c in diag2 or c in cols:
                continue

            diag1.add(r+c)
            diag2.add(r-c)
            cols.add(c)

            res += self.totalNQueens(N, diag1, diag2, cols, r+1)

            diag1.remove(r+c)
            diag2.remove(r-c)
            cols.remove(c)

        return res


class Solution:
    def totalNQueens(self, N: int, i=0, seen=set(), res=0) -> int:
        """
        Backtracking
        """
        if i == N:
            res += 1

        for j in range(N):
            place = {("col", j), ("diag", i-j), ("anti", i+j)}
            if not (place & seen):
                seen |= place
                res = self.totalNQueens(N, i+1, seen, res)
                seen -= place

        return res
