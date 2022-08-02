"""
1358. Number of Substrings Containing All Three Characters
Medium

Given a string s consisting only of characters a, b and c.Return the number of substrings containing at least one occurrence of all these characters a, b and c.

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




import collections
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
    """
    Sliding window
    """
    freq = {x: 0 for x in 'abc'}
    res = left = 0
    for right in range(len(s)):
        freq[s[right]] += 1
        while all(freq.values()):
            freq[s[left]] -= 1
            left += 1
        res += left

    return res


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Time: O(N), Space O(1) since we always going to have 3 elements stored (a,b,c)  
        and this won't change even if our string was a million characters long.
        """
        j, res = 0, 0
        freq = collections.Counter()
        for i, c in enumerate(s):
            freq[c] += 1
            while len(freq) == 3:
                res += len(s) - i
                freq[s[j]] -= 1
                if not freq[s[j]]:
                    freq.pop(s[j])
                j += 1
        return res


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Maintain a window which contains at least each character of a, b, c.
        Once we found a window, rest part of that window will be a valid count.
        So we can add len(s) - left on it.
        Time: O(N), Space O(1) since we always going to have 3 elements stored (a,b,c)  
        and this won't change even if our string was a million characters long.
        """
        freq = defaultdict(int)
        left, N = 0, len(s)
        res = 0
        for right, c in enumerate(s):
            freq[c] += 1
            while len(freq) >= 3:
                res += N - right
                freq[s[left]] -= 1
                if not freq[s[left]]:
                    freq.pop(s[left])
                left += 1
        return res


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, res = [-1]*3, 0
        for i, x in enumerate(s):
            a[ord(x)-ord('a')] = i
            res += min(a)+1
        return res
