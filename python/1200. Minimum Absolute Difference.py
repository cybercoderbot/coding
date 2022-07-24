"""
1200. Minimum Absolute Difference
Easy

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
"""


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        MIN = min(b - a for a, b in zip(arr[:-1], arr[1:]))
        return [[a, b] for a, b in zip(arr[:-1], arr[1:]) if b - a == MIN]


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        diff = inf
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] <= diff:
                if arr[i] - arr[i-1] < diff:
                    res = []
                    diff = arr[i] - arr[i-1]
                res.append([arr[i-1], arr[i]])
        return res
