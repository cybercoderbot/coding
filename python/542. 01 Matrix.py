"""
542. 01 Matrix
Medium

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])
        front = set((i, j) for i in range(M)
                    for j in range(N) if not matrix[i][j])  # frontier
        visited = front.copy()  # visited cell

        d = 0
        while front:
            nextfront = set()
            for x, y in front:
                matrix[x][y] = d
                for i, j in (x-1, y), (x, y-1), (x, y+1), (x+1, y):
                    if 0 <= i < M and 0 <= j < N and (i, j) not in visited:
                        nextfront.add((i, j))
            front = nextfront
            visited = visited | nextfront
            d += 1
        return matrix
