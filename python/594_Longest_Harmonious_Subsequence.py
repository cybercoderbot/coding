class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        # Let count[x] be the number of x's in our array.
        # Suppose our longest subsequence B has min(B) = x and max(B) = x+1.
        # Evidently, it should use all occurrences of x and x+1 to maximize it's length, 
        # so len(B) = count[x] + count[x+1].
        # Additionally, it must use x and x+1 at least once, so count[x] and count[x+1] should both be positive.
        
        count = collections.Counter(nums)
        ans = 0
        for x in count:
            if x+1 in count:
                ans = max(ans, count[x] + count[x+1])
                
        return ans
        
        
        
        
        
