"""
77. Combinations
Medium

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.


Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(first, comb):
            # if the combination is done
            if len(comb) == k:
                res.append(comb[:])

            for i in range(first, n + 1):
                # add i into the current combination
                comb.append(i)
                # use next integers to complete the combination
                backtrack(i+1, comb)
                # backtrack
                comb.pop()

        res = []
        backtrack(1, [])

        return res
