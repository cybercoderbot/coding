class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        # 判断输入单词的字母集合是否为键盘某一行字母集合的子集

        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')

        result = []
        for word in words:
            w = set(word.lower())
            if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
                result.append(word)
        return result
