/*Given an array of integers, every element appears twice except for one. Find that single one.*/

/*这道题让我们找到一组数中出现次数一次的数，但是由于加上了时间复杂度必须是O(n)，并且空间复杂度为O(1)，
使得不能用排序方法，也不能使用map数据结构。那么只能另辟蹊径，需要用位操作Bit Operation来解此题。
由于数字在计算机是以二进制存储的，每位上都是0或1，如果我们把两个相同的数字异或，0与0异或是0,
1与1异或也是0，那么我们会得到0。根据这个特点，我们把数组中所有的数字都异或起来，则每对相同的数字
都会得0，然后最后剩下来的数字就是那个只有1次的数字*/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int n : nums){
            ans = n ^ ans;
        }
        return ans;
    }
};


