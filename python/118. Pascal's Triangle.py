"""
118. Pascal's Triangle
Easy

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: 
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Example 2:
Input: numRows = 1
Output: [[1]]
"""


class Solution:
    def generate(self, N: int) -> List[List[int]]:
        if N == 0:
            return []
        if N == 1:
            return [[1]]
        if N == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]
        for i in range(2, N):
            row = []
            for j in range(i-1):
                row.append(sum(res[-1][j:j+2]))
            res.append([1] + row + [1])

        return res


class Solution:
    def generate(self, N: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(N):
            row = [a + b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(row)
        return res[:N]


class Solution:
    def generate(self, N: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, N):
            res += [map(lambda x, y: x+y, res[-1]+[0], [0]+res[-1])]
        return res[:N]


class Solution:
    def generate(self, N: int) -> List[List[int]]:
        res, row = [], []
        for i in range(N):
            row.append(1)
            for j in range(i-1, 0, -1):
                row[j] += row[j-1]
            res.append(row.copy())
        return res


class Solution:
    def getRow(self, k: int) -> List[int]:
        """
        119. Pascal's Triangle II
        Given an integer k, return the kth row of the Pascal's triangle.
        """
        res = []
        for _ in range(k+1):
            res.append(1)
            for i in range(len(res)-2, 0, -1):
                res[i] += res[i-1]
        return res
