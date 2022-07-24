"""
923. 3Sum With Multiplicity
Medium


Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.


Example 1:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20

Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12

Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

Example 3:
Input: arr = [2,1,3], target = 6
Output: 1

Explanation: (1, 2, 3) occured one time in the array so we return 1.
"""


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        Time: O(N^2)
        Space:O(N)
        """
        res = 0
        seen = defaultdict(int)

        for i, n in enumerate(arr):
            res += seen[target-n]
            for j in range(i):
                sm = arr[j] + arr[i]
                seen[sm] += 1

        return res % (10**9+7)
