"""
1275. Find Winner on a Tic Tac Toe Game
Easy

Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

Example 1:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
Instead of harcoding 3 all over the place. Solve for n * n grid and set n = 3 in the beginning. That way the code is scalable and there will just be a one line change if the interviewer asks your for a 4x4 grid.

Storing the rows and cols as array of size n + 2 variables for diagonals and reverse diagonal. This requires less memory O(2N + 2) instead of O(n^2)
Also checking if a player has won or not takes O(1) time as I have to check 4 variables.
The logic is to increment(Player A) and decrement(Player B) the row, col and the 2 diagonal variables depending on who played and which row, col was played.
After every move, we need to check if the value of the row, col, or the diagonal variables is 3 or -3. Whoever played in that turn is the winner.
Time Complexity for every move check: O(1)
Space Complexity: O(N)
"""


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        isA = True
        N = 3
        rows = [0] * N
        cols = [0] * N
        diag1, diag2 = 0, 0

        for r, c in moves:
            move = 1 if isA else -1
            rows[r] += move
            cols[c] += move
            if r == c:
                diag1 += move
            if r + c == N-1:
                diag2 += move

            if N in [abs(rows[r]), abs(cols[c]), abs(diag1), abs(diag2)]:
                return "A" if isA else "B"

            isA = not isA

        return "Draw" if len(moves) == N * N else "Pending"


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        N = 3
        rows, cols = [0] * N, [0] * N
        diag1 = diag2 = 0

        for index, move in enumerate(moves):
            i, j = move
            sign = 1 if index % 2 == 0 else -1
            rows[i] += sign
            cols[j] += sign
            if i == j:
                diag1 += sign
            if i + j == N-1:
                diag2 += sign
            if N in [abs(rows[i]), abs(cols[j]), abs(diag1), abs(diag2)]:
                return 'A' if sign == 1 else 'B'

        return "Draw" if len(moves) == N * N else 'Pending'
