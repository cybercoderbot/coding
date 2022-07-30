"""
84. Largest Rectangle in Histogram
Hard

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Use a stack to store non-decreasing height.
        At position i, pop all heights (by index) that is higher than heights[i] from stack.

        Height is obtained from the poped index.
        Width is obtained by index i and last value on stack.
        """

        # non-decreasing mono-stack
        stack = []

        res = 0
        heights.append(0)

        for i, x in enumerate(heights):

            while stack and heights[stack[-1]] > x:
                depth = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                res = max(res, depth * width)

            stack.append(i)

        return res
