class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # # 字符统计 + 排序
        # collections.Counter(s).most_common([n])
        # Return a list of the n most common elements and their counts from the most common to the least. 
        # If n is omitted or None, most_common() returns all elements in the counter.
        
        
        # >>> from collections import Counter
        # >>> Counter('abracadabra').most_common(3)
        # [('a', 5), ('b', 2), ('r', 2)]
        # >>> Counter('abracadabra').most_common()
        # [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
        # >>> s = 'abracadabra'
        # >>> ans = ''.join(e * cnt for e, cnt in collections.Counter(s).most_common())
        #     ans ='aaaaabbrrcd'

        
        c_with_count = collections.Counter(s).most_common()
        return ''.join(c * cnt for c, cnt in c_with_count)
        
        
        
        
        
        
