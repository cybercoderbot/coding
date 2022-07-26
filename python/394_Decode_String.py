class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 迭代的方法：
        # 需要用stack来辅助运算，我们用两个stack，一个用来保存个数，一个用来保存字符串，
        # 我们遍历输入字符串，如果遇到数字，我们更新计数变量cnt；如果遇到左括号，我们把当前cnt压入数字栈中，
        # 把当前t压入字符串栈中；如果遇到右括号时，我们取出数字栈中顶元素，存入变量k，然后给字符串栈的顶元素
        # 循环加上k个t字符串，然后取出顶元素存入字符串t中；如果遇到字母，我们直接加入字符串t中即可

        # 当出现左括号时，将字符串压栈。
        # 当出现右括号时，将字符串弹栈，并重复响应次数，累加至新的栈顶元素。

        k = 0
        strs = collections.defaultdict(str)
        nums = collections.defaultdict(int)

        for i in range(len(s)):
            if s[i].isdigit():
                nums[k] = nums[k] * 10 + int(s[i])
            elif s[i] == '[':
                k += 1
            elif s[i] == ']':
                strs[k - 1] += nums[k - 1] * strs[k]
                nums[k - 1] = 0
                strs[k] = ''
                k -= 1
            else:
                strs[k] += s[i]
        return strs[0]
