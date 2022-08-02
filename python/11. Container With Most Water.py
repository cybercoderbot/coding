"""
11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Brute Force
        simply consider the area for every possible pair of the lines and 
        find out the maximum area out of those. 
        Time: O(N^2), Space: O(1)
        """
        res = 0
        N = len(height) - 1

        for left in range(N):
            for right in range(left + 1, N):
                width = right - left
                depth = min(height[left], height[right])
                res = max(res, depth * width)

        return res


"""
Approach 2: Two Pointer Approach

The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, the farther the lines, the more will be the area obtained.

We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. Futher, we maintain a variable maxarea to store the maximum area obtained till now. At every step, we find out the area formed between them, update maxarea and move the pointer pointing to the shorter line towards the other end by one step.

The algorithm can be better understood by looking at the example below:

How does this approach work?

Initially we consider the area constituting the exterior most lines. Now, to maximize the area, we need to consider the area between the lines of larger lengths. If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the reduction in the width. This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction.

Complexity Analysis

Time complexity: O(N). Single pass.

Space complexity: O(1). Constant space is used.
"""


class Solution(object):
    def maxArea(self, height: List[int]) -> int:
        """
        Two pointers
        Time: O(N), Space: O(1)
        """
        N = len(height)
        left, right = 0, N-1

        res = 0
        while left < right:
            width = right - left
            depth = min(height[left], height[right])
            res = max(res,  width * depth)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
