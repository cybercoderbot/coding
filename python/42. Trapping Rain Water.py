"""
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Mono-stack 
        """
        res = 0
        stack = []
        for i, x in enumerate(height):
            while stack and stack[-1][1] <= x:
                _, pre = stack.pop()
                if stack:
                    width = i - stack[-1][0] - 1
                    depth = min(stack[-1][1], x) - pre
                    res += width * depth
            stack.append((i, x))
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Two pointers 
        Keep track of the maximum height from both forward directions backward directions, call them left and right. Use two pointers to scan the entire array until they meet with each other. Key points: any bars in the middle of left bar and right bar will not influence
        how much water can current position trap
        https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution.
        """

        i, j = 0, len(height)-1
        left, right, res = 0, 0, 0

        while i <= j:
            left = max(left, height[i])
            right = max(right, height[j])

            if left < right:
                res += left - height[i]
                i += 1
            else:
                res += right - height[j]
                j -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Two pointers (can be extended to 2D case)

        Maintain two pointers i and j pointing to the lower and upper bound respectively.

        1) if height[i] < height[j], i += 1
        2) otherwise, j -= 1

        In the meantime, keep track of the maximum depth of left and right respectively, and compute volume when moving the pointer as the difference of left or right and the corresponding height.
        """
        i, j = 0, len(height)-1
        res = depth = 0

        while i < j:
            if height[i] <= height[j]:
                depth = max(depth, height[i])
                res += depth - height[i]
                i += 1
            else:
                depth = max(depth, height[j])
                res += depth - height[j]
                j -= 1

        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Top-down DP
        """
        left = []
        for x in height:
            if not left:
                left.append(x)
            else:
                left.append(max(left[-1], x))

        res = 0
        right, N = 0, len(height)
        for i in range(N-1, -1, -1):
            right = max(right, height[i])
            res += min(left[i], right) - height[i]
        return res
