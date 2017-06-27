/*把已经算过的节点用哈希表保存起来，以后递归调用的时候，现在哈希表里找，如果存在直接返回，如果不存在，等计算出来后，
保存到哈希表中再返回，这样方便以后再调用*/

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
    int rob(TreeNode* root) {
        unordered_map<TreeNode*, int> m;
        return dfs(root, m);
    }
    
    int dfs(TreeNode* root, unordered_map<TreeNode*, int>& m){
        if (!root) return 0;
        if (m.count(root)) return m[root];
        int val = 0;
        if (root->left)
            val += dfs(root->left->left, m) + dfs(root->left->right, m);
            
        if (root->right)
            val += dfs(root->right->left, m) + dfs(root->right->right, m);
        
        val = max(val + root->val, dfs(root->left, m) + dfs(root->right, m));
        m[root] = val;
        return val;
    }
};





