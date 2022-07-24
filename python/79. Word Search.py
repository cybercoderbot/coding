"""
79. Word Search
Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false"""


"""

I'd consider this problem backtracking although many use "dfs" to categorize it. 
Here, a useful trick is to check if there are more occurrences of a letter in word than in board. 
If so, we can directly return False. 
This is a non-essential step, but dramatically improves the performance.

"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if Counter(word) - Counter(sum(board, [])):
            return False

        M, N = len(board), len(board[0])

        def found(i, j, k):
            """Return true if a match is found."""
            if board[i][j] == word[k]:
                if k == len(word)-1:
                    return True
                temp = board[i][j]
                board[i][j] = None  # mark as used
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                    inbound = 0 <= ii < M and 0 <= jj < N
                    if inbound and board[ii][jj] and found(ii, jj, k+1):
                        return True
                board[i][j] = temp
            return False

        return any(found(i, j, 0) for i, j in product(range(M), range(N)))


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])

        def found(i, j, k):
            """Return True if a match is found."""
            if k == len(word)-1:
                return True
            temp = board[i][j]
            board[i][j] = '#'
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                inbound = 0 <= ii < M and 0 <= jj < N
                if inbound and board[ii][jj] == word[k+1] and found(ii, jj, k+1):
                    return True
            board[i][j] = temp
            return False

        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0] and found(i, j, 0):
                    return True
        return False
