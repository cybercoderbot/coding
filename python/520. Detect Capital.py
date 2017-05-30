class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        # 这道题给了我们一个单词，让我们检测大写格式是否正确，规定了三种正确方式，要么都是大写或小写，
        # 要么首字母大写，其他情况都不正确。那么我们要做的就是统计出单词中所有大写字母的个数cnt，
        # 再来判断是否属于这三种情况，如果cnt为0，说明都是小写，正确；如果cnt和单词长度相等，说明都是大写，正确；
        # 如果cnt为1，且首字母为大写，正确，其他情况均返回false
        
        count = 0
        n = len(word)
        for c in word:
            if c <= 'Z':
                count += 1
            
        return count==0 or count==n or (count == 1 and word[0] <='Z')
        
        # return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())
        
        
        
