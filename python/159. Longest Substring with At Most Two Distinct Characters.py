"""
159. Longest Substring with At Most Two Distinct Characters
Medium

Given a string s, return the length of the longest substring that contains at most two distinct characters.

Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
"""

"""
Here, we can imagine a queue of size 2 with distinct characters. 
Once a new character arrives, we check if it is the same as the end of queue
* if so, do nothing
* if not, pop from the front
if the poped character is different from the newly arrived one, update starting anchor(ii)

"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Time: O(N), Space: O(N)
        """
        res = j = 0
        x0 = x1 = ""
        seen = {"": -1}  # last seen
        for i, x in enumerate(s):
            if x1 != x:
                if x0 != x:
                    j = seen[x0] + 1
                x0, x1 = x1, x
            seen[x] = i
            res = max(res, i - j + 1)
        return res


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Time: O(N), Space: O(N)
        """
        res, j = 0, -1  # starting anchor
        queue = collections.deque()
        seen = {}  # last seen
        for i, x in enumerate(s):
            if not queue or queue[-1] != x:
                queue.append(x)
            if len(queue) > 2:
                y = queue.popleft()
                if y != x:
                    j = seen[y]  # update anchor
            res = max(res, i - j)
            seen[x] = i
        return res
