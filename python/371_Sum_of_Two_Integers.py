class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        # 这道题让我们实现两数相加，但是不能用加号或者其他什么数学运算符号，
        # 那么我们只能回归计算机运算的本质，位操作Bit Manipulation，我们在做加法运算的时候，
        # 每位相加之后可能会有进位Carry产生，然后在下一位计算时需要加上进位一起运算，
        # 那么我们能不能将两部分拆开呢，我们来看一个例子759+674

        # 1. 如果我们不考虑进位，可以得到323
        
        # 2. 如果我们只考虑进位，可以得到1110
        
        # 3. 我们把上面两个数字假期323+1110=1433就是最终结果了

        # 然后我们进一步分析，如果得到上面的第一第二种情况，我们在二进制下来看，
        # 不考虑进位的加，0+0=0， 0+1=1, 1+0=1， 1+1=0，这就是异或的运算规则，
        # 只考虑进位的加0+0=0, 0+1=0, 1+0=0, 1+1=1，而这其实这就是与的运算，
        # 而第三步在将两者相加时，我们再递归调用这个算法，终止条件是当进位为0时，
        # 我们直接返回第一步的结果
        
        # if b==0: return a
        # sum_ = a^b
        # carry = (a & b) << 1
        # return self.getSum(sum_, carry)
        
        # max int32
        # MAX_INT = 0x7FFFFFFF
        # MASK = 0x100000000
        # while b:
        #     carry = ((a&b) << 1 ) % MASK
        #     a = (a^b) % MASK
        #     b = carry
            
        # if a <= MAX_INT:
        #     return a 
        # else:
        #     return ~((a & MAX_INT) ^ MAX_INT)
        
        MAX_INT = 0x7FFFFFFF
        MASK = 0x100000000
        while b:
            carry = ((a&b) << 1 ) % MASK
            a = (a^b) % MASK
            b = carry
            
        if a <= MAX_INT:
            return a 
        else:
            return ~((a & MAX_INT) ^ MAX_INT)
            
            
        # MAX_INT = 0x7FFFFFFF
        # MIN_INT = 0x80000000
        # MASK = 0x100000000
        # while b:
        #     a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        # return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
            
        
        # for _ in range(32):
        #     a, b = a^b, (a&b)<<1
            
        # if a & 0x80000000:
        #     return a
        # else:
        #     return a & 0xffffffff
            
            
        # MAX_INT = 0x7FFFFFFF
        # MASK = 0x100000000
        # while b:
        #     a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        # return a if a <= MAX_INT else ~((a & MAX_INT) ^ MAX_INT)
        
        
