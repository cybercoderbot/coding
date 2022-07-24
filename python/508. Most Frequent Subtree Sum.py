"""
508. Most Frequent Subtree Sum
Medium


Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

 

Example 1:
Input: root = [5,2,-3]
Output: [2,-3,4]

Example 2:
Input: root = [5,2,-5]
Output: [2]
"""


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node):
            """Populate frequency table."""
            if not node:
                return 0
            res = node.val + dfs(node.left) + dfs(node.right)
            freq[res] += 1
            return res

        freq = defaultdict(int)
        dfs(root)
        mode = max(freq.values(), default=0)
        return [k for k, v in freq.items() if v == mode]
