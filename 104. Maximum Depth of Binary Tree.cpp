/*Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node 
down to the farthest leaf node.*/
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
    int maxDepth(TreeNode* root) {
        /*求二叉树的最大深度问题用到深度优先搜索DFS，递归的完美应用，
        跟求二叉树的最小深度问题原理相同*/
        if (!root) return 0;
        int d_left = maxDepth(root->left);
        int d_right = maxDepth(root->right);
        return max(d_left, d_right) + 1;
    }
};



