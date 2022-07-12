class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 3 != 0) { return false; }
        int target = sum / 3;
        int cursum = 0, count = 0;
        for (int n : nums) {
            cursum += n;
            if (cursum == target) {
                count++;
                cursum = 0;
            }
        }
        return count >= 3;

    }
};