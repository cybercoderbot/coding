class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //O(n)的算法：遍历数组，建立map数据，遍历的同时开始查找，找到则记录index
        unordered_map<int, int> m;
        for(int i=0; i<nums.size(); i++){
            int d = target-nums[i];
            if(m.count(d)){
                return {i, m[d]};
            }else{
                m[nums[i]] = i;
            }
        }
        return {};
        
    }
};
