/*Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.*/

/*这道题的本质是遍历二叉树，所以我们可以用 Level Order Traverse + queue，注意对左子叶的判断和处理*/

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
    int sumOfLeftLeaves(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> q;
        q.push(root);
        int ans = 0;
        while (!q.empty()){
            TreeNode* n = q.front();
            q.pop();
            if (n->left && !n->left->left && !n->left->right){
                ans += n->left->val;
            }
            if (n->left) q.push(n->left);
            if (n->right) q.push(n->right);
        }
        return ans;
    }
};


/*我们也可以用stack, 跟上面的解法几乎一样，只是把queue换成了stack，q.front()换成了s.top(), 实际上遍历的顺序不同*/
class Solution{
public:
    int sumOfLeftLeaves(TreeNode* root){
        if (!root) return 0;
        stack<TreeNode*> s;
        s.push(root);
        int ans = 0;
        while (!s.empty()){
            TreeNode* n = s.top();
            s.pop();
            if (n->left && !n->left->left && !n->left->right){
                ans += n->left->val;
            }
            if (n->left) s.push(n->left);
            if (n->right) s.push(n->right);
        }
        return ans;
    }
};

