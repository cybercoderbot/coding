/*697.Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the 
maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the 
same degree as nums.

Example 1:

Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
 

Example 2:

Input: [1,2,2,3,1,4,2]
Output: 6
 

Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999. */
 

/*这道题给了我们一个数组，定义数组的度为某个或某些数字出现最多的次数，要我们找最短的子数组使其和原数组拥有相同的度。
那么我们肯定需要统计每个数字出现的次数，就要用哈希表来建立每个数字和其出现次数之间的映射。由于我们要求包含原度的最小
长度的子数组，那么最好的情况就是子数组的首位数字都是统计度的数字，即出现最多的数字。那么我们肯定要知道该数字的第一次
出现的位置和最后一次出现的位置，由于我们开始不知道哪些数字会出现最多次，所以我们统计所有数字的首尾出现位置，那么我们
再用一个哈希表，建立每个数字和其首尾出现的位置。我们用变量degree来表示数组的度。好，现在我们遍历原数组，累加当前数字
出现的次数，当某个数字是第一次出现，那么我们用当前位置的来更新该数字出现的首尾位置，否则只更新尾位置。每遍历一个数，
我们都更新一下degree。当遍历完成后，我们已经有了数组的度，还有每个数字首尾出现的位置，下面就来找出现次数为degree的数组，
然后计算其首尾位置差加1就是candidate数组的长度，由于出现次数为degree的数字不一定只有一个，我们遍历所有的，找出其中最小
的即可*/

 

class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        int n = nums.size(), res = INT_MAX, degree = 0;
        unordered_map<int, int> m;
        unordered_map<int, pair<int, int>> pos;
        for (int i = 0; i < nums.size(); ++i) {
            if (++m[nums[i]] == 1) {
                pos[nums[i]] = {i, i};
            } else {
                pos[nums[i]].second = i;
            }
            degree = max(degree, m[nums[i]]);
        }
        for (auto a : m) {
            if (degree == a.second) {
                res = min(res, pos[a.first].second - pos[a.first].first + 1);
            }
        }
        return res;
    }
};




