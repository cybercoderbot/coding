class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 解题思路：
        # BFS（广度优先搜索）
        # 将当前单词拆分为前后两半，若前缀可以在字典dict中找到，则将后缀加入队列。


        queue = [s]
        to_visit = set([s])
        while queue:
            front = queue.pop(0)
            if front in wordDict:
                return True
            prefix = ''
            for c in front:
                prefix += c
                suffix = front[len(prefix):]
                if prefix in wordDict and suffix not in to_visit:
                    queue.append(suffix)
                    to_visit.add(suffix)
        return False
        
        
        
        
