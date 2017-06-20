/*Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longestpath between any two nodes in a tree. 
This path may or may not pass through the root.

Example:
Given a binary tree 

          1
         / \
        2   3
       / \     
      4   5    
 

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.*/

/*Post-order traverse, 在深度的递归函数中顺便把直径算出*/

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
    int diameterOfBinaryTree(TreeNode* root) {
        int ans = 0;
        maxDepth(root, ans);
        return ans;
    }
    int maxDepth(TreeNode* node, int& ans) {
        if (!node) return 0;
        int left = maxDepth(node->left, ans);
        int right = maxDepth(node->right, ans);
        ans = max(ans, left + right);
        return max(left, right) + 1;
    }
};


