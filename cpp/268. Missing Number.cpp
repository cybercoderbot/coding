/*Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
For example,
Given nums = [0, 1, 3] return 2.*/

/*思路:0到n之间少了一个数，我们将这个少了一个数的数组合0到n之间完整的数组异或一下，那么相同的数字都变为0了，剩下的就是少了的那个数字了*/

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans = 0;
        for (int n=1; n <= nums.size(); n++){
            ans ^= n ^ nums[n-1];
        }
        return ans;
    }
};


/*0到n之间的数但是有一个数字去掉了，让我们寻找这个数字，要求线性的时间复杂度和常数级的空间复杂度。另一个直观的方法是用等差数列的求和公式
求出0到n之间所有的数字之和，然后再遍历数组算出给定数字的累积和，然后做减法，差值就是丢失的那个数字*/

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum = 0, n = nums.size();
        for (auto &x : nums) {
            sum += x;
        }
        return  n * (n + 1)/2 - sum;
    }
};




