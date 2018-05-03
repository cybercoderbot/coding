/*Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as 
possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

这道题让我们分割数组，两两一对，让每对中较小的数的和最大。这题难度不大，用greedt algori就可以了。
由于我们要最大化每对中的较小值之和，那么肯定是每对中两个数字大小越接近越好，因为如果差距过大，
而我们只取较小的数字，那么大数字就浪费掉了。明白了这一点，我们只需要给数组排个序，然后按顺序的
每两个就是一对，我们取出每对中的第一个数即为较小值累加起来即可

Inorder to maximize the summation, we have to make the difference between each pair as small as possible,
otherwise the larger number is sacrificed. It's very similar to the bucket theory: a bucket can only fill 
with the volume of water the shortest plank allows.
*/



class Solution {
public:
    int arrayPairSum(vector<int>& nums) {        
        int ans = 0;
        sort(nums.begin(), nums.end());
        for (int i=0; i<nums.size(); i+=2){
            ans += nums[i];
        }
        return ans;
    }
};




