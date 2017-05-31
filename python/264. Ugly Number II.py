class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
     

        # 丑陋数序列可以拆分为下面3个子列表：

        # (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
        # (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
        # (3) 1×5, 2×5, 3×5, 4×5, 5×5, …
        # 我们可以发现每一个子列表都是丑陋数本身(1, 2, 3, 4, 5, …) 乘以 2, 3, 5
        
        # 接下来我们使用与Merge Sort相似的合并方法，从3个子列表中获取丑陋数。
        # 每一步我们从中选出最小的一个，然后向后移动一步。


        dp = [1]
        i2 = i3 = i5 = 0
        
        while len(dp) < n:
            x2 = dp[i2] * 2
            x3 = dp[i3] * 3
            x5 = dp[i5] * 5
            
            xn = min(x2, x3, x5)
            
            if xn == x2: i2 += 1
            if xn == x3: i3 += 1
            if xn == x5: i5 += 1
                
            dp.append(xn)
            
        return dp[-1]
        
        
        
        
        
