class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        # 解题思路: 记忆化搜索
        # 在搜索过程中，使用字典ansDict将已经搜索过的子句的拆解方案记录下来，从而实现DFS的剪枝。

        ansDict = {}
        
        def dfs(s):
            ans = []
            if s in wordDict:
                ans.append(s)
                
            for i in range(len(s) - 1):
                prefix, suffix = s[:i+1], s[i+1:]
                if prefix not in wordDict:
                    continue
                # rest = []
                if suffix in ansDict:
                    rest = ansDict[suffix]
                else:
                    rest = dfs(suffix)
                for n in rest:
                    ans.append(prefix + ' ' + n)
            ansDict[s] = ans
            return ans
            
        return dfs(s)
        
        
        
