class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
        vector<int> result;
        for (int i=0; i<heights.size(); i++){
            
            while (!result.empty() && heights[result.back()] <= heights[i]){
                result.pop_back();
            }
            result.push_back(i);
        }
        return result;
    }
};