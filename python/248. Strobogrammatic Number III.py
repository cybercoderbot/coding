"""
248. Strobogrammatic Number III
Hard

Given two strings low and high that represent two integers low and high where low <= high, return the number of strobogrammatic numbers in the range [low, high].

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:
Input: low = "50", high = "100"
Output: 3

Example 2:
Input: low = "0", high = "0"
Output: 1
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        """
        246. Is Strobogrammatic Number ("69", "88", etc)
        """
        pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]
        i, j = 0, len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in pairs:
                return False
            i += 1
            j -= 1
        return True


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        """
        246. Is Strobogrammatic Number ("69", "88", etc)
        """
        pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]
        return all((num[i], num[-(i+1)]) in pairs for i in range(len(num)//2+1))


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        """
        247. Strobogrammatic Number II
        Return all the strobogrammatic numbers that are of length n.
        """
        if n == 1:
            return ["0", "1", "8"]

        def strobo(n):
            """Return strobogrammatic number with length n."""

            pairs = ["00", "11", "69", "88", "96"]

            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]
            return [x+z+y for x, y in pairs for z in strobo(n-2)]

        return [x for x in strobo(n) if not x.startswith("0")]


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        """
        248. Strobogrammatic Number III
        Return the number of strobogrammatic numbers in the range [low, high].
        """

        pairs = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        stack = ["", "0", "1", "8"]
        res = 0
        while stack:
            word = stack.pop()
            if len(word) < len(high) or len(word) == len(high) and word <= high:
                if len(word) > len(low) or len(word) == len(low) and word >= low:
                    res += word == "0" or not word.startswith("0")
                if len(high) - len(word) >= 2:
                    for x, y in pairs.items():
                        stack.append(x + word + y)
        return res


class Solution:
    res = 0

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        """
        248. Strobogrammatic Number III
        Return the number of strobogrammatic numbers in the range [low, high].
        """
        for i in range(len(low), len(high) + 1):
            for d in ['', '1', '8', '0']:
                self.dfs(low, high, i, d)
        return self.res

    def dfs(self, low, high, length, path):
        # leng = len(path)
        if len(path) > length:
            return
        if len(path) == length:
            if len(path) != 1 and path[0] == '0':
                return
            elif int(low) <= int(path) <= int(high):
                self.res += 1
            return
        for d in ['00', '69', '96', '88', '11']:
            self.dfs(low, high, length, d[0] + path + d[1])
