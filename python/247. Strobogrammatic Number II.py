"""
247. Strobogrammatic Number II
Medium

Given an integer n, return all the strobogrammatic numbers that are of length n. 
You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:
Input: n = 2
Output: ["11","69","88","96"]

Example 2:
Input: n = 1
Output: ["0","1","8"]
"""


def strobo(n):
    """Return strobogrammatic number of length n."""

    pairs = ["00", "11", "69", "88", "96"]

    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1", "8"]

    return [p+x+q for p, q in pairs for x in strobo(n-2)]


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        res = strobo(n)
        if n == 1:
            return res
        else:
            return [x for x in res if not x.startswith("0")]
