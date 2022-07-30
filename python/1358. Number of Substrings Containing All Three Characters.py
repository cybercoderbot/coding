"""
1358. Number of Substrings Containing All Three Characters
Medium

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".

Example 3:
Input: s = "abc"
Output: 1
"""

"""
This is the sliding window problem, when it satisfies the requirements (containing all three characters), we move i (i++). That means after the while loop, i-1 would be the leftmost index to satisfy the requirements, i doesn't satisfy (break the while loop).
[i-1, j] would be the minimum window size to satisfy the requirements.
Because it is minimal, we can choose nums[0], nums[1] ... nums[i-1] as the left side of the window, which still satisfies the requirement
Therefore, we can add i new cases (from 0 to i -1) to res.
"""


def numberOfSubstrings(self, s):
    """
    Sliding window
    """
    res = i = 0
    count = {c: 0 for c in 'abc'}

    for j in xrange(len(s)):
        count[s[j]] += 1
        while all(count.values()):
            count[s[i]] -= 1
            i += 1
        res += i

    return res


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, res = [-1]*3, 0
        for i, x in enumerate(s):
            a[ord(x)-ord('a')] = i
            res += min(a)+1
        return res
