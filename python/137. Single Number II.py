class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 这道题就是除了一个单独的数字之外，数组中其他的数字都出现了三次，那么还是要利用位操作 Bit Operation 来解此题。
        # 我们可以建立一个32位的数字，来统计每一位上1出现的个数，我们知道如果某一位上为1的话，那么如果该整数出现了三次，
        # 对3去余为0，我们把每个数的对应位都加起来对3取余，最终剩下来的那个数就是单独的数字
        
        # 32 bits for each integer. Consider 1 bit in it, the sum of each integer's corresponding bit
        # (except for the single number) should be 0 if mod by 3. Hence, we sum the bits of all integers
        # and mod by 3, the remaining should be the exact bit of the single number. In this way, you get
        # the 32 bits of the single number
        
        ans = 0
        for i in range(32):
            count = 0
            for n in nums:
                if (n >> i) & 1:
                    count+=1
            ans = ans | (count%3) << i
        return ans if ans < 2**31 else ans - 2**32
        
        
        
        
        
        
