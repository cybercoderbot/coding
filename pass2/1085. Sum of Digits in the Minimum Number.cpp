class Solution {
public:
    int sumOfDigits(vector<int>& nums) {
        int minval = *min_element(nums.begin(), nums.end());
        int sum = 0;
        while(minval != 0){
            sum += minval % 10;
            minval /= 10;
        }
        return sum % 2 == 0 ? 1 : 0;
    }
};