/*You are a professional robber planning to rob houses along a street. Each house has a certain amount of money 
stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system 
connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.*/

/*对于这类求极值的问题首先考虑动态规划Dynamic Programming来解，递推公式dp[i] = max(dp[i-2] + num[i], dp[i-1])*/

class Solution {
public:
    int rob(vector<int> &num) {
        if (num.size() <= 1) return num.empty() ? 0 : num[0];
        vector<int> dp = {num[0], max(num[0], num[1])};
        for (int i = 2; i < num.size(); i++) {
            dp[i] = max(num[i] + dp[i-2], dp[i-1]);
        }
        return dp.back();
    }
};




