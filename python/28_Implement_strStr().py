# 28. Implement strStr() Add to List
# Implement strStr().
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 这道题让我们在一个字符串中找另一个字符串第一次出现的位置，那我们首先要做一些判断，
        # 如果子字符串为空，则返回0，如果子字符串长度大于母字符串长度，则返回-1。
        
        # 然后我们开始遍历母字符串，我们并不需要遍历整个母字符串，而是遍历到剩下的长度和子字符串
        # 相等的位置即可，这样可以提高运算效率。然后对于每一个字符，我们都遍历一遍子字符串，一个
        # 一个字符的对应比较，如果对应位置有不等的，则跳出循环，如果一直都没有跳出循环，则说明子
        # 字符串出现了，则返回起始位置即可
        
        # Time complexity: O(n*m).
        
        if not needle or not haystack: 
            return 0
            
        m = len(haystack)
        n = len(needle)
        
        if m < n: return -1
        
        for i in range(m-n+1):
            if haystack[i: i+n] == needle:
                return i
        return -1
        
        
        
        
