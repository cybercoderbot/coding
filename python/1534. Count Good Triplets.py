"""
1534. Count Good Triplets
Easy

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

 

Example 1:

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
Example 2:

Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.

"""


class Solution:
    def countGoodTriplets(self, nums: List[int], a: int, b: int, c: int) -> int:

        res, N = 0, len(nums)

        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    ok_a = abs(nums[i] - nums[j]) <= a
                    ok_b = abs(nums[j] - nums[k]) <= b
                    ok_c = abs(nums[i] - nums[k]) <= c

                    if ok_a and ok_b and ok_c:
                        res += 1

        return res
