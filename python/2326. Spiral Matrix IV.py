"""
2326. Spiral Matrix IV
Medium

You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

Example 1:
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.

Example 2:
Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def spiralMatrix(self, M: int, N: int, head: Optional[ListNode]) -> List[List[int]]:
        """
        1) Initial: di, dj = 0, 1
        2) If out of bound: di, dj = dj, -di
        3) Update: i, j = i+di, j+dj
        """

        i, j = 0, 0
        di, dj = 0, 1
        res = [[-1]*N for _ in range(M)]

        node = head
        while node:
            res[i][j] = node.val
            node = node.next
            if not (0 <= i+di < M and 0 <= j+dj < N and res[i+di][j+dj] == -1):
                di, dj = dj, -di
            i, j = i+di, j+dj

        return res
