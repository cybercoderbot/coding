class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 这道题让我们找一个范围内的各位上不相同的数字，比如123就是各位不相同的数字，而11,121,222
        # 就不是这样的数字。那么我们根据提示中的最后一条可以知道，一位数的满足要求的数字是10个(0到9)，
        # 二位数的满足题意的是81个，[10~99]这90个数字中去掉[11,22,33,44,55,66,77,88,99]这9个数字，
        # 还剩81个。f(k) = 长度为k的不重复数位的数字个数, 通项公式为f(k) = 9 * 9 * 8 * ... (9-k+2)，
        # 那么我们就可以根据n的大小，把[1, n]区间位数通过通项公式算出来累加起来即可

        nums = [9]
        for x in range(9, 0, -1):
            print(nums)
            nums.append(nums[-1] * x)
        # print(sum(nums[:n]) + 1)
        return sum(nums[:n]) + 1

        # nums:
        # [9]
        # [9, 81]
        # [9, 81, 648]
        # [9, 81, 648, 4536]
        # [9, 81, 648, 4536, 27216]
        # [9, 81, 648, 4536, 27216, 136080]
        # [9, 81, 648, 4536, 27216, 136080, 544320]
        # [9, 81, 648, 4536, 27216, 136080, 544320, 1632960]
        # [9, 81, 648, 4536, 27216, 136080, 544320, 1632960, 3265920]
