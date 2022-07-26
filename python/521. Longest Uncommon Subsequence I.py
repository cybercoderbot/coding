class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """

        # 这道题让我们找两个string的longest uncommon subsequence，
        # 如果两个字符串相等，那么一定没有uncommon subsequence，
        # 反之，如果两个字符串不等，那么较长的那个字符串就是最长非共同子序列

        if a == b:
            return -1
        else:
            return max(len(a), len(b))
