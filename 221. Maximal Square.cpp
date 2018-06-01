/*Maximal Square 

Given a 2D binary grid filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following grid:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.
*/

class Solution {
public:
    int maximalSquare(vector<vector<char>> &grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        int m = grid.size(), n = grid[0].size(), res = 0;
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 || j == 0) dp[i][j] = grid[i][j] - '0';
                else if (grid[i][j] == '1') {
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1;
                }
                res = max(res, dp[i][j]);
            }
        }
        return res * res;
    }
};
