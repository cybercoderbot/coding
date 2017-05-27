class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        
        # Depth: the number of tabs 
        # For each depth the current path length is stored
        
        # 这道题给了我们一个字符串，里面包含\n和\t这种表示回车和空格的特殊字符，让我们找到
        # 某一个最长的绝对文件路径，要注意的是，最长绝对文件路径不一定是要最深的路径，我们
        # 可以用哈希表来建立深度depth和当前深度的绝对路径长度pathlen之间的映射，那么当前深度下的文件的
        # 绝对路径就是文件名长度len(name)加上哈希表中当前深度对应的长度，我们的思路是遍历整个字符串，
        # 遇到\n或者\t就停下来，然后我们判断，如果遇到的是回车，我们把这段文件名提取出来，
        # 如果里面包含'.'，说明是文件，我们更新maxlen长度，如果不包含点，说明是文件夹，我们深度depth
        # 增1，然后建立当前深度和总长度之间的映射，然后我们将深度depth重置为0。之前如
        # 果遇到的是空格\t，那么我们深度加一，通过累加\t的个数，我们可以得知当前文件或文件夹
        # 的深度，然后做对应的处理
        
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth+1] = pathlen[depth] + len(name) + 1
        return maxlen
        
        
        
        
