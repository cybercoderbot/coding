/* 653. Two Sum IV - Input is a BST
Given a Binary Search Tree and a target number, return true if there exist two elements
 in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

*/



/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <unordered_set>

class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        if(!root){
            return false;
        }
        std::unordered_set<int> s;
        return find(root, k, s);
    }
    bool find(TreeNode* node, int k, std::unordered_set<int> &s){
        if(!node){
            return false;
        }
        int d = k - node->val;
        if (s.count(d)){
            return true;
        }else{
            s.insert(node->val);
            return find(node->left, k, s) || find(node->right, k, s);
        }
    }
};