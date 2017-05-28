class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        
        # 解题思路：
        # 深度优先搜索（DFS）+ 剪枝（Pruning）
        # 首先构建一个 单词前缀prefix->单词word 的字典d
        # 深度优先搜索search(word, line)，其中word是当前单词，line是行数
        # 利用变量matrix记录当前已经生成的单词
        # 前缀prefix = matrix[0..line][line]，如果prefix对应单词不存在，则可以剪枝
        # 否则枚举d[prefix]，并递归搜索

        
        nrow = len(words)
        ncol = len(words[0]) if nrow else 0
        d = collections.defaultdict(set)
        for w in words:
            for i in range(ncol):
                d[w[:i]].add(w)
        matrix = []
        ans = []
        
        def search(word, line):
            matrix.append(word)
            if line == ncol:
                ans.append(matrix[:])
            else:
                prefix = ''.join(matrix[x][line] for x in range(line))
                for word in d[prefix]:
                    search(word, line + 1)
            matrix.pop()
            
        for w in words:
            search(w, 1)
        return ans


