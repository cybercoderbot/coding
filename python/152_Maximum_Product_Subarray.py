class Solution(object):
    def maxProduct(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 解题思路：Dynamic programming

        # 用数组positive_max[i]维护原始数组前i个数的子数组乘积中正数的最大值
        # 用数组negative_min[i]维护原始数组前i个数的子数组乘积中负数的最小值
        
        # 状态转移方程为：
        
        # if A[x] > 0:
        # 	positive_max[x] = max(positive_max[x-1] * A[x], A[x])
        # 	negative_min[x] = negative_min[x-1] * A[x]
        
        # elif A[x] < 0:
        # 	positive_max[x] = negative_min[x-1] * A[x]
        # 	negative_min[x] = min(positive_max[x-1] * A[x], A[x])
        	
	
        ans = max(A)
        size = len(A)
        positive_max = [0 for x in range(size)]
        negative_min = [0 for x in range(size)]
        
        if A[0] > 0: positive_max[0] = A[0]
        elif A[0] < 0: negative_min[0] = A[0]
        	
        for x in range(1, size):
        	if A[x] > 0:
        		positive_max[x] = max(positive_max[x-1] * A[x], A[x])
        		negative_min[x] = negative_min[x-1] * A[x]
        		
        	elif A[x] < 0:
        		positive_max[x] = negative_min[x-1] * A[x]
        		negative_min[x] = min(positive_max[x-1] * A[x], A[x])
        		
    		ans = max(ans, positive_max[x])
    		
        return ans
        
        
        
        
