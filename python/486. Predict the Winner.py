class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
        486. Predict the Winner
        """
        N = len(nums)
        if N % 2 == 0:
            return True

        dp = nums[:]
        for i in range(1, N):
            for j in range(N-i):
                dp[j] = max(nums[j]-dp[j+1], nums[j+i]-dp[j])
        return dp[0] >= 0
