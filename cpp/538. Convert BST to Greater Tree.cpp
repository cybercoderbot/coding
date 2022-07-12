/** 538. Convert BST to Greater Tree
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key 
of the original BST is changed to the original key plus sum of all keys greater 
than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
 */

// Solution: In-order traverse (iterative method)
class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        if(!root) return NULL;
        int sum = 0;
        stack<TreeNode*> s;
        TreeNode *p = root;
        while(p || !s.empty()){
            while(p){
                s.push(p);
                p = p->right;
            }
            p = s.top(); s.pop();
            p->val += sum;
            sum = p->val;
            p = p->left;
        }
        return root;
    }
};