"""
37. Sudoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.


Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


"""


"""
Solution:
Progressively try filling empty spots and backtrack when the current setup isn't working.
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        empty = []
        seen = set()

        for i, j in product(range(9), range(9)):
            x = board[i][j]
            if x == ".":
                empty.append((i, j))
            else:
                seen.add((i, x))
                seen.add((x, j))
                seen.add((i//3, x, j//3))

        def backtrack(k):
            if k == len(empty):
                return True

            i, j = empty[k]

            for x in "123456789":
                if any([(i, x) in seen, (x, j) in seen, (i//3, x, j//3) in seen]):
                    continue

                board[i][j] = x
                seen.add((i, x))
                seen.add((x, j))
                seen.add((i//3, x, j//3))

                if backtrack(k+1):
                    return True
                else:
                    seen.remove((i, x))
                    seen.remove((x, j))
                    seen.remove((i//3, x, j//3))

        backtrack(0)

        return


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        empty = []
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    seen |= {(i, board[i][j]), (board[i][j],
                                                j), (i//3, board[i][j], j//3)}

        def fn(k, seen):
            if k == len(empty):
                return True
            i, j = empty[k]
            for x in "123456789":
                if seen & {(i, x), (x, j), (i//3, x, j//3)}:
                    continue
                seen |= {(i, x), (x, j), (i//3, x, j//3)}
                board[i][j] = x
                if fn(k+1, seen):
                    return True
                seen -= {(i, x), (x, j), (i//3, x, j//3)}

        fn(0, seen)

        return


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        spots = []  # empty spots
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sub = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spots.append((i, j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    sub[i//3*3+j//3].add(board[i][j])

        def fn(k):
            """return True if kth spot is filled properly"""
            if k == len(spots):
                return True
            i, j = spots[k]
            for n in map(str, range(1, 10)):
                if n not in row[i] and n not in col[j] and n not in sub[i//3*3+j//3]:
                    board[i][j] = n
                    row[i].add(n)
                    col[j].add(n)
                    sub[i//3*3+j//3].add(n)
                    if fn(k+1):
                        return True
                    else:
                        row[i].remove(n)
                        col[j].remove(n)
                        sub[i//3*3+j//3].remove(n)
            return False

        fn(0)  # change in place
