"""
55. Jump Game
Medium

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        i, maxPos = 0, 0

        while i <= maxPos:
            maxPos = max(maxPos, i + nums[i])
            if maxPos >= N - 1:
                return True
            i += 1

        return False


"""
45. Jump Game II
Medium

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.


Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2"""


class Solution:

    def jump(self, nums):
        N = len(nums)
        if N <= 1:
            return 0
        left, right = 0, nums[0]
        res = 1
        while right < N - 1:
            res += 1
            nxt = max(i + nums[i] for i in range(left, right + 1))
            left, right = right, nxt
        return res


"""
1306. Jump Game III
Medium

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.


Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

Example 2:
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

Example 3:
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
"""


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        queue = [start]

        while queue:
            node = queue.pop(0)

            if arr[node] == 0:
                return True

            for i in [node + arr[node], node - arr[node]]:
                if 0 <= i < N:
                    queue.append(i)

            # mark as visited
            arr[node] = -arr[node]

        return False
