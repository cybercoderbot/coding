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
        
        # if s in wordDict: return True

        queue = [s]
        while queue:
            front = queue.pop(0)
            if front in wordDict:
                return True
            prefix = ''
            for c in front:
                prefix += c
                suffix = front[len(prefix):]
                if prefix in wordDict and suffix not in queue:
                    queue.append(suffix)
        return False
        
        
