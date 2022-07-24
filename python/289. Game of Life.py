"""
289. Game of Life
Medium

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.


Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]


Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


"""

"""
# The key to in-place operation is almost always to properly code the matrix so that the info is kept. For this problem, when we mark a cell live (i.e. 1) or dead (i.e. 0), we can overshoot the numbers. Namely, when changing 1 to 0 we overshoot it to -1; when changing 0 to 1, we overshoot it to 2. Then, -1 means that the cell was live but is dead now, while 2 means that the cell was dead but is live now. In this way, the info of previous state was kept.
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])  # dimensions

        for i, j in product(range(M), range(N)):
            count = 0
            for ii, jj in product(range(i-1, i+2), range(j-1, j+2)):
                isValidNeighbor = 0 <= ii < M and 0 <= jj < N and (
                    i, j) != (ii, jj)
                if isValidNeighbor and abs(board[ii][jj]) == 1:
                    count += 1
            if board[i][j] and (count < 2 or count > 3):
                board[i][j] = -1  # live to dead
            elif not board[i][j] and count == 3:
                board[i][j] = 2  # dead to live

        for i, j in product(range(M), range(N)):
            board[i][j] = int(board[i][j] > 0)
