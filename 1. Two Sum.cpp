class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //O(n)的算法：遍历数组，建立map数据，遍历的同时开始查找，找到则记录index
    
        unordered_map<int, int> m;
        for(int i=0; i<nums.size(); i++){
            if(m.count(target-nums[i])){
                return {i, m[target-nums[i]]};
            }
            m[nums[i]] = i;
        }
        return {};
        
    }
};
