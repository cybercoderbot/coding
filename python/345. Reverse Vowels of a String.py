class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # two pointers
        # 这道题让我们翻转字符串中的元音字母，元音字母有五个a,e,i,o,u，需要注意的是大写的也算，
        # 所以总共有十个字母。我们判断当前字符是否为元音字母，如果两边都是元音字母，那么我们交换，
        # 如果左边的不是，向右移动一位，如果右边的不是，则向左移动一位
        # Strings can be swapped; must be converted to list for swapping and converted back for string

        vowels = 'aeiou'
        left, right = 0, len(s)-1
        ls = list(s)

        while left < right:
            c1 = s[left].lower()
            c2 = s[right].lower()
            if c1 in vowels and c2 in vowels:
                ls[left], ls[right] = ls[right], ls[left]
                left += 1
                right -= 1
            elif c1 in vowels:
                right -= 1
            else:
                left += 1
        return ''.join(ls)

        # wrong
        # vowels = 'aeiou'
        # left, right = 0, len(s)-1
        # ls = list(s.lower())
        # # ['h', 'e', 'l', 'l', 'o']

        # while left < right:
        #     while s[left] not in vowels:
        #         left += 1
        #     while s[right] not in vowels:
        #         right -= 1
        #     ls[left], ls[right] = ls[right], ls[left]
        #     left += 1
        #     right -= 1

        # return ''.join(ls)
