class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> comb;
        solveDFS(candidates, target, result, comb, 0);
        return result;
    }
    
    void solveDFS(vector<int>& candidates, int target, vector<vector<int>>& result, vector<int>& comb, int start){
        if (target<0) {
            return;
        }
        if (target==0){
            result.push_back(comb);
            return;
        }
        for (int i=start; i<candidates.size(); i++){
            comb.push_back(candidates[i]);
            solveDFS(candidates, target-candidates[i], result, comb, i);
            comb.pop_back();
        }

    }
};
