"""
503. Next Greater Element II
Medium

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
"""


class Solution(object):
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Approach 1 - backward
        Decreasing mono-stack

        Time: O(N)
        Space: O(N)
        """

        stack = nums[::-1]
        res = []

        for x in reversed(nums):
            while stack and x >= stack[-1]:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(x)

        res.reverse()

        return res


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Approach 1 - backward
        Decreasing mono-stack

        Loop Twice
        Loop once, we can get the Next Greater Number of a normal array.
        Loop twice, we can get the Next Greater Number of a circular array

        Time: O(N)
        Space: O(N)
        """

        res, stack = [], []
        for x in reversed(nums + nums):
            while stack and x >= stack[-1]:
                stack.pop()
            ans.append(stack[-1] if stack else -1)
            stack.append(x)
        res.reverse()
        return res[:len(nums)]


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Approach 2 - forward

        Loop Twice
        Loop once, we can get the Next Greater Number of a normal array.
        Loop twice, we can get the Next Greater Number of a circular array

        Time: O(N)
        Space: O(N)
        """

        res = [-1] * len(nums)
        stack = []

        for i, x in enumerate(nums + nums):
            while stack and stack[-1][1] < x:
                k, _ = stack.pop()
                res[k] = x
            stack.append((i % len(nums), x))

        return res


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)

        # [0, 1, 2] * 2 -> [0, 1, 2, 0, 1,2] * 2
        for i in list(range(len(nums))) * 2:
            while stack and nums[stack[-1]] < nums[i]:
                k = stack.pop()
                res[k] = nums[i]
            stack.append(i)
        return res
