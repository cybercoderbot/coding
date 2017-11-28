/*Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and 
the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1 */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
/*Solution: POSTORDER Tree traverse + DFS*/

class Solution {
public:
    int findTilt(TreeNode* root) {
        if(!root) return 0;
        int res = 0;
        postorder(root, res);
        return res;
    }
    
private:
    int postorder(TreeNode* node, int& res){
        if(!node) return 0;
        int lsum = postorder(node->left,res);
        int rsum = postorder(node->right,res);
        res += abs(lsum - rsum);
        return lsum + rsum + node->val;
        
    }
};

