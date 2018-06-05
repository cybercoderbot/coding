/*Given an array where elements are sorted in ascending order, convert it to a height balanced BST.*/

/*这道题是要将有序数组转为二叉搜索树，二叉搜索树始终满足左<根<右的特性，如果将二叉搜索树按中序遍历的话，得到的就是一个有序数组了。
那么反过来，根节点应该是有序数组的中间点，从中间点分开为左右两个有序数组，在分别找出其中间点作为原中间点的左右两个子节点，这就是
二分查找法的核心思想*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (!nums.size()) return 0;
        int mid = nums.size() / 2;
        TreeNode* root = new TreeNode(nums[mid]);
        vector<int> numsLeft (nums.begin(), nums.begin() + mid);
        vector<int> numsRight (nums.begin() + mid + 1, nums.end());
        root->left =  sortedArrayToBST(numsLeft);
        root->right = sortedArrayToBST(numsRight);
        return root;
    }
};



