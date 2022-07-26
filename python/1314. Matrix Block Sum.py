"""
1314. Matrix Block Sum
Medium

Given a m x n matrix mat and an integer k, 
return a matrix where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
 

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
"""


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        csum = [[0]*(N+1) for _ in range(M+1)]

        for i, j in product(range(M), range(N)):
            csum[i+1][j+1] = csum[i][j+1] + \
                csum[i+1][j] + mat[i][j] - csum[i][j]

        res = [[0]*N for _ in range(M)]
        for i, j in product(range(M), range(N)):
            r0, r1 = max(0, i-k), min(M-1, i+k)
            c0, c1 = max(0, j-k), min(N-1, j+k)
            res[i][j] = csum[r1+1][c1+1] - csum[r0][c1+1] - \
                csum[r1+1][c0] + csum[r0][c0]
        return res


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        M, N = len(mat), len(mat[0])
        dp = [[0]*(N+1) for _ in range(M+1)]

        for i, j in product(range(M), range(N)):
            dp[i+1][j+1] = mat[i][j] + dp[i+1][j] + dp[i][j+1] - dp[i][j]

        for i, j in product(range(M), range(N)):
            r2 = i+K+1 if i+K+1 < M+1 else M
            r1 = i-K if i-K >= 0 else 0
            c2 = j+K+1 if j+K+1 < N+1 else N
            c1 = j-K if j-K >= 0 else 0
            mat[i][j] = dp[r2][c2] - dp[r2][c1] - dp[r1][c2] + dp[r1][c1]

        return mat
