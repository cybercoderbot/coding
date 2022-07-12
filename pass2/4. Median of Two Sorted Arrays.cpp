class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int i=0, j=0;
        int m = nums1.size();
        int n = nums2.size();
        vector<int> nums{};
        while (i<m && j<n){
            if (nums1[i] < nums2[j]){
                nums.push_back(nums1[i]);
                i++;
            } else {
                nums.push_back(nums2[j]); 
                j++;
            }
        }
        if (i>=m && j<n){
            for (; j<n; j++){
                nums.push_back(nums2[j]); 
            }
        }
        if (j>=n && i<m){
            for (; i<m; i++){
                nums.push_back(nums1[i]); 
            }
        }
        
        if ((m+n)%2!=0){
            return nums[(m+n)/2];
        }else{
            return (nums[(m+n)/2-1] + nums[(m+n)/2] ) / 2.0;
        }
    }
};