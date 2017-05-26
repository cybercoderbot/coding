class Solution(object):


    # 解题思路：
    # 首先将输入字符串列表strs按照长度递减排序，记得到的新列表为 s_sorted
    # 利用计数器count统计每个字符串出现的次数。
    # 遍历 s_sorted，记当前字符串为c，其下标为i：
    #     若c在strs中出现不止一次，跳过该字符串
    #     否则，利用贪心算法对c和s_sorted[0 .. i-1]的字符串进行匹配，若均匹配失败，则返回len(c)
    # 遍历结束，返回-1


    def uncommon(self, x, y):
        i = j = 0
        while i < len(x) and j < len(y):
            if x[i] == y[j]:
                j += 1
            i += 1
        return j != len(y)


    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        count = collections.Counter(strs)
        s_sorted = sorted(set(strs), key=len, reverse=True)

        for i, c in enumerate(s_sorted):
            if count[c] > 1:
                continue
            for p in s_sorted:
                comp = [self.uncommon(p,c) for p in s_sorted[:i] ]
                if all(comp):
                    return len(c)

        return -1
        
        
        
        
