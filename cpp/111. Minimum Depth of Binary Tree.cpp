/**
111. Minimum Depth of Binary Tree
DescriptionHintsSubmissionsDiscussSolution

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.

 */

int minDepth(TreeNode* root) {
    if(!root) return 0;
    else if(!root->left && !root->right) return 1;
    else if(!root->left) return minDepth(root->right) + 1;
    else if(!root->right) return minDepth(root->left) + 1;
    else return min(minDepth(root->left), minDepth(root->right)) + 1;
    
}
