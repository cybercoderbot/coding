class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 这道题在之前那道题Max Consecutive Ones的基础上加了一个条件，说我们有一次将0翻转成1的机会，
        # 问此时最大连续1的个数，再看看follow up中的说明，很明显是让我们只遍历一次数组，那我们想，
        # 肯定需要用一个变量cnt来记录连续1的个数吧，那么当遇到了0的时候怎么处理呢，因为我们有一次
        # 0变1的机会，所以我们遇到0了还是要累加count，然后我们此时需要用另外一个变量prev来保存当前count
        # 的值，然后count重置为0，以便于让count一直用来统计纯连续1的个数，然后我们每次都用用count+prev来
        # 更新结果ans
        
        ans, prev, count = 0, 0, 0
        
        for n in nums:
            count += 1
            if n==0:
                prev = count
                count = 0
            ans = max(ans, count + prev)
        return ans
        
        
        
        
