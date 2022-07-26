class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        # 题目大意：
        # 给定一组长度为偶数的整数，其中每个数字代表一个糖果的种类标号。
        # 将糖果均分给哥哥和妹妹，返回妹妹可以得到的最大糖果种类数。

        # 解题思路：
        # 返回 min( 糖果总数的一半, 糖果种类数 ) 即可

        return min(len(candies)/2, len(set(candies)))
