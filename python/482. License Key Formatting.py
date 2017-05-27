class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        # 字符串模拟
        # 将S的开头部分用'#'补足，使其长度是K的整数倍，返回时将#删去
        s = s.replace('-', '').upper()
        if len(s) % k:
            m = k - len(s) % k 
            s = '#' * m + s
        idx = range(0, len(s), k)
        tmp = [s[i:i+k] for i in idx]
        return '-'.join(tmp).replace('#', '')
        
        
        
        
        
