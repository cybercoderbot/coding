/*Given a binary array, find the maximum number of consecutive 1s in this array.
Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.*/

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        /*这道题让我们求最大连续1的个数，我们可以遍历一遍数组，用一个计数器count来统计1的个数，
        方法是如果当前数字为0，那么count重置为0，如果不是0，count自增1，然后每次更新结果ans即可*/
        if (nums.empty()) return 0;
        int ans = 0, count = 0;
        for (int n : nums){
            count = (count + 1) * n;
            ans = max(ans, count);
        }
        return ans;
    }
};




