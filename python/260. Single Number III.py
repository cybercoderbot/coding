class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 这道题是之前那两道Single Number 单独的数字和 Single Number II 单独的数字之二的再次延伸，
        # 那道题其实是很巧妙的利用了Single Number 单独的数字的解法，准确的找出只出现了一次的数字，
        # 但前提是其他数字必须出现两次才行。而这题有两个数字都只出现了一次，那么我们如果能想办法把
        # 原数组分为两个小数组，不相同的两个数字分别在两个小数组中，这样分别调用Single Number 单独的数字
        # 的解法就可以得到答案。那么如何实现呢，首先我们先把原数组全部异或起来，那么我们会得到一个数字，
        # 这个数字是两个不相同的数字异或的结果，我们取出其中任意一位为‘1’的位，为了方便起见，我们用 a &= -a
        # 来取出最右端为‘1’的位，然后和原数组中的数字挨个相与，那么我们要求的两个不同的数字就被分到了两个小组中，
        # 分别将两个小组中的数字都异或起来，就可以得到最终结果了

        # result of a^b
        axb = reduce(lambda x, y: x ^ y, nums)
        lowbit = axb & -axb
        a = b = 0
        for n in nums:
            if n & lowbit:
                a = a ^ n
            else:
                b = b ^ n
        return [a, b]
