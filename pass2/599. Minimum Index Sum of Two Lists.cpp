class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        vector<string> res;
        unordered_map<string, int> map;
        int smallest_index = INT_MAX;
        
        for (int i=0; i<list1.size(); i++){
            map[list1[i]] = i;
        }
        
        for (int i=0; i<list2.size(); i++){
            if (map.count(list2[i])){
                int sum_index = i + map[list2[i]];
                if (sum_index == smallest_index){
                    res.push_back(list2[i]);
                } else if (sum_index < smallest_index){
                    smallest_index = sum_index;
                    res = {list2[i]};
                }
            }
            
        }
        return res;
        
    }
};