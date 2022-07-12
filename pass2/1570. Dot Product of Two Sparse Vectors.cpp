class SparseVector {
    unordered_map<int,int> m;
public:
    
    SparseVector(vector<int> &nums) {
        for (int i=0; i<nums.size(); i++){
            if (nums[i]!=0) { m[i] = nums[i]; }
        }
    }
    
    // Return the dotProduct of two sparse vectors
    int dotProduct(SparseVector& vec) {
        int sum = 0;
        for (auto x : m){
            if(vec.m.find(x.first) != vec.m.end()) {
                sum += vec.m[x.first] * x.second;
            }
        }
        return sum;
    }
};


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n!=0:
                self.nonzeros[i] = n
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result
        