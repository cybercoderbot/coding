/*Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node 
down to the farthest leaf node.
Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.
*/

int maxDepth(TreeNode* root) {
    if (!root) return 0;
    int d_left = maxDepth(root->left);
    int d_right = maxDepth(root->right);
    return max(d_left, d_right) + 1;
}




