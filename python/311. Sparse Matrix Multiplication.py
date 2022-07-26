"""
311. Sparse Matrix Multiplication
Medium

882

308

Add to List

Share
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

 

Example 1:


Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]
Example 2:

Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]
"""


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        Time complexity O(MKN)
        Space complexity O(MN)
        """
        M, K, N = len(A), len(B), len(B[0])  # dimensions
        res = [[0] * N for _ in range(M)]

        for i, k in product(range(M), range(K)):
            if not A[i][k]:
                continue
            for j in range(N):
                if not B[k][j]:
                    continue
                res[i][j] += A[i][k] * B[k][j]

        return res
