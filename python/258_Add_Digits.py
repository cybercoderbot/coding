class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 这道题让我们求数根，所谓树根，就是将大于10的数的各个位上的数字相加，若结果还大于0的话，
        # 则继续相加，直到数字小于10为止。那么根据这个性质，我们可以写出一个解法如下：

        while num > 9:
            c = 0
            while num:
                c += num % 10
                num /= 10
            num = c
        return num

        # 通过先来观察1到20的所有的输出，可以得出规律，每9个一循环，所有大于9的数的树根都是对9取余，
        # 那么对于等于9的数对9取余就是0了，为了得到其本身，而且同样也要对大于9的数适用，
        # 我们就用(n-1)%9+1这个表达式来包括所有的情况，所以解法如下：

        if num == 0:
            return 0
        return (num-1) % 9 + 1
