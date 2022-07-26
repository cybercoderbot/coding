class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """

        # 这道题定义了一种对称数，就是说一个数字旋转180度和原来一样，也就是倒过来看一样，
        # 比如609，倒过来还是609等等，满足这种条件的数字其实没有几个，只有0,1,8,6,9。
        # 这道题其实可以看做求回文数的一种特殊情况，我们还是用双指针来检测.
        # 首尾两个数字如果相等的话，那么只有它们是0,1,8中间的一个才行，
        # 如果不相等的话，必须一个是6一个是9，或一个是9一个是6，其他所有情况均返回False

        left, right = 0, len(num)-1

        while left <= right:
            if not self.strob(num[left], num[right]):
                return False
            left += 1
            right -= 1
        return True

    def strob(self, c1, c2):
        if c1 == c2 and c1 in '018':
            return True
        elif (c1, c2) in (('6', '9'), ('9', '6')):
            return True

        return False
