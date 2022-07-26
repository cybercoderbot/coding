"""
1035. Uncrossed Lines
Medium

You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

Example 2:
Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
"""


from functools import lru_cache


# Same as 1143. Longest Common Subsequence

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Top-down

        Time complexity O(MN)
        Space complexity O(MN)
        """

        @lru_cache(None)
        def uncrossed(i, j):
            """Return length of longest common subsequence of nums1[i:] and nums2[j:]"""
            if i == len(nums1) or j == len(nums2):
                return 0

            if nums1[i] == nums2[j]:
                return uncrossed(i+1, j+1) + 1
            else:
                return max(uncrossed(i+1, j), uncrossed(i, j+1))

        return uncrossed(0, 0)


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Bottom-up
        """
        m, n = len(nums1), len(nums2)  # dimensions
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Bottom-up with space optimization
        """
        dp = [0]*(1 + len(nums2))
        for i in reversed(range(len(nums1))):
            tmp = dp.copy()
            for j in reversed(range(len(nums2))):
                if nums1[i] == nums2[j]:
                    dp[j] = 1 + tmp[j+1]
                else:
                    dp[j] = max(tmp[j], dp[j+1])
        return dp[0]
