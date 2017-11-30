/*
Print Binary Tree

Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.

Example 1:

Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]


Example 2:

Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]


Example 3:

Input:
      1
     / \
    2   5
   /
  3
 /
4
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]


Note: The height of binary tree is in the range of [1, 10].
*/

/*
这道题给了我们一棵二叉树，让我们以数组的形式打印出来。数组每一行的宽度是二叉树的最底层数所能有的最多结点数，
存在的结点需要填入到正确的位置上。那么这道题我们就应该首先要确定返回数组的宽度，由于宽度跟数组的深度有关，
所以我们首先应该算出二叉树的最大深度，直接写一个子函数返回这个最大深度，从而计算出宽度。下面就是要遍历二叉树
从而在数组中加入结点值。我们先来看第一行，由于根结点只有一个，所以第一行只需要插入一个数字，不管这一行多少
个位置，我们都是在最中间的位置插入结点值。下面来看第二行，我们仔细观察可以发现，如果我们将这一行分为左右
两部分，那么插入的位置还是在每一部分的中间位置，这样我们只要能确定分成的部分的左右边界位置，就知道插入结点
的位置了，所以应该是使用分治法的思路。在递归函数中，如果当前node不存在或者当前深度超过了最大深度直接返回，
否则就给中间位置赋值为结点值，然后对于左子结点，范围是左边界到中间位置，调用递归函数，注意当前深度加1；
同理对于右子结点，范围是中间位置加1到右边界，调用递归函数，注意当前深度加1
*/

using namespace std;

class Solution {
public:
    vector<vector<string>> printTree(TreeNode* root) {
        int h = getHeight(root), w = pow(2, h) - 1;
        vector<vector<string>> res(h, vector<string>(w, ""));
        helper(root, 0, w - 1, 0, h, res);
        return res;
    }
    void helper(TreeNode* node, int i, int j, int curH, int height, vector<vector<string>>& res) {
        if (!node || curH == height) return;
        res[curH][(i + j) / 2] = to_string(node->val);
        helper(node->left, i, (i + j) / 2, curH + 1, height, res);
        helper(node->right, (i + j) / 2 + 1, j, curH + 1, height, res);
    }
    int getHeight(TreeNode* node) {
        if (!node) return 0;
        return 1 + max(getHeight(node->left), getHeight(node->right));
    }
};
