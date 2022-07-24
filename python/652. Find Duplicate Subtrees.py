"""
652. Find Duplicate Subtrees
Medium


Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.


Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
"""


"""
Traverse the tree in post-order dfs and in the meantime serialize the sub-tree 
to check if the same serialization has been seen.

"""


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        def serialize(node):
            """Return serialized sub-tree rooted at node."""
            if not node:
                return " "

            left = serialize(node.left)
            right = serialize(node.right)
            string = ",".join((str(node.val), left, right))

            if seen[string] == 1:
                res.append(node)

            seen[string] += 1

            return string

        res = []
        seen = defaultdict(int)
        serialize(root)

        return res
