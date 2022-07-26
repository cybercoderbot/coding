class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        # 这道题让求从一个字符串转变到另一个字符串需要的变换步骤，共有三种变换方式，插入一个字符，删除一个字符，和替换一个字符。
        # 根据以往的经验，对于字符串相关的题目十有八九都是用动态规划Dynamic Programming来解，这道题也不例外。这道题我们需要维护
        # 一个二维的数组dp，其中dp[i][j]表示从word1的前i个字符转换到word2的前j个字符所需要的步骤。那我们可以先给这个二维数组dp的
        # 第一行第一列赋值，这个很简单，因为第一行和第一列对应的总有一个字符串是空串，于是转换步骤完全是另一个字符串的长度。跟以
        # 往的DP题目类似，难点还是在于找出递推式，我们可以举个例子来看，比如word1是“bbc"，word2是”abcd“，那么我们可以得到dp数组如下：

        #   Ø a b c d
        # Ø 0 1 2 3 4
        # b 1 1 1 2 3
        # b 2 2 1 2 3
        # c 3 3 2 1 2

        # 我们通过观察可以发现，当word1[i] == word2[j]时，dp[i][j] = dp[i-1][j-1]，
        # 其他情况时，dp[i][j]是其左，左上，上的三个值中的最小值加1，那么可以得到递推式为：

        #                  / dp[i-1][j-1],                                       if word1[i - 1] == word2[j - 1]
        #     dp[i][j] =
        #                  \ min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1, else

        # O(m*n) space, O(m*n) time
        n1 = len(word1)+1
        n2 = len(word2)+1

        dp = [[0 for _ in range(n2)] for _ in range(n1)]

        for i in range(n1):
            dp[i][0] = i

        for j in range(n2):
            dp[0][j] = j

        for i in range(1, n1):
            for j in range(1, n2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

        return dp[-1][-1]
