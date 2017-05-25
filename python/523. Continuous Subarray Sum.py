class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        # 给我们一个数组和一个数字k，让我们求是否存在这样的一个连续的子数组，该子数组的数组之和可以整除k。
        # 遇到除法问题，我们肯定不能忘了除数为0的情况等处理。还有就是我们如何能快速的遍历所有的子数组，并且求和，
        # 我们肯定不能完全的暴力破解，这样OJ肯定不答应。我们需要适当的优化，遇到这种求子数组或者子矩阵之和的题，
        # 应该不难想到要建立累加和数组或者累加和矩阵来做。我们要遍历所有的子数组，然后利用累加和来快速求和。
        # 在得到每个子数组之和时，我们先和k比较，如果相同直接返回true，否则再判断，若k不为0，且sum能整除k，
        # 同样返回true，最后遍历结束返回false


        n = len(nums)
        for i in range(n):
            cumsum = nums[i]
            for j in range(i+1, n):
                cumsum += nums[j]
                if cumsum == k:
                    return True
                if k!=0 and cumsum%k == 0:
                    return True
        return False
        
        
        # 下面这种方法用了些技巧，那就是，若数字a和b分别除以数字c，若得到的余数相同，那么(a-b)必定能够整除c.
        
        # if   a = k1 * c + n
        #      b = k2 * c + n
        
        # then a-b = (k1-k2) * c
        
        # 我们用一个dictionary来建立余数和当前位置之间的映射，如果当前的累加和除以k得到的余数在d中已经存在了，
        # 那么说明之前必定有一段子数组和可以整除k。若两个index差大于2,则满足题意，返回true。
        # 需要注意的是k为0的情况，由于无法取余，我们就把当前累加和cumsum放入d中。
    
        
        d = {0: -1}
        cumsum = 0
        
        for i, n in enumerate(nums):
            cumsum += n
            if k:
                # remainder
                r = cumsum % k
            else:
                r = cumsum
                
            if r not in d: 
                d[r] = i
            elif d[r] + 2 <= i: 
                return True
        return False





