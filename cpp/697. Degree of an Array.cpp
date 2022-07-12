/*697. Degree of an Array
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
*/

/*这种方法只用了一次遍历，就要建立数字出现次数的哈希表，还有就是建立每个数字和其第一次出现位置之间的映射，那么我们
当前遍历的位置其实可以看作是尾位置，还是可以计算子数组的长度的。我们遍历数组，累加当前数字出现的次数，如果某个数字
是第一次出现，建立该数字和当前位置的映射，如果当前数字的出现次数等于degree时，当前位置为尾位置，首位置在startIdx中取的，
二者做差加1来更新结果res；如果当前数字的出现次数大于degree，说明之前的结果代表的数字不是出现最多的，直接将结果res
更新为当前数字的首尾差加1的长度，然后degree也更新为当前数字出现的次数*/

class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        int res = INT_MAX;
        int degree = 0;
        unordered_map<int, int> m;
        unordered_map<int, int> startIdx;
        int i = 0;
        for (auto n : nums) {
            m[n]++;
            if (!startIdx.count(n)) startIdx[n] = i;
            if (m[n] == degree) {
                res = min(res, i - startIdx[n] + 1);
            } else if (m[n] > degree) {
                res = i - startIdx[n] + 1;
                degree = m[n];
            }
            i++;
        }
        return res; 
    }
};