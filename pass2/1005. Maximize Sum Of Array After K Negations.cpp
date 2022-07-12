class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        int res = 0;
        int minval = INT_MAX;
        sort(nums.begin(), nums.end());
        for (int i=0; nums[i] <0 && i<nums.size() && k>0; i++, k--){
            nums[i] *= -1;
        }
        for (int n : nums){
            res += n;
            minval = min(minval, n);
        } 
        return res - 2 *(k%2) * minval;
    }
    
};