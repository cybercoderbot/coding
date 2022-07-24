"""
437. Path Sum III
Medium

7979

379

Add to List

Share
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        seen = {0: 1}
        
        def dfs(node, prefix):
            """Return number of paths summing to target for tree rooted at node."""
            # base condition 
            if not node: 
                return 0 
            prefix += node.val # prefix sum up to node 
            res = seen.get(prefix-target, 0)
            seen[prefix] = seen.get(prefix, 0) + 1
            res += dfs(node.left, prefix) 
            res += dfs(node.right, prefix)
            seen[prefix] -= 1 # backtrack 
            return res
        
        return dfs(root, 0)



class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:

        def preorder(node: TreeNode, cumsum) -> None:
            nonlocal count
            if not node:
                return 
            
            # current prefix sum
            cumsum += node.val
            
            # here is the sum we're looking for
            if cumsum == target:
                count += 1
            
            # number of times the cumsum − k has occurred already, 
            # determines the number of times a path with sum k 
            # has occurred up to the current node
            count += freq[cumsum - target]
            
            # add the current sum into hashmap
            # to use it during the child nodes processing
            freq[cumsum] += 1
            
            # process left subtree
            preorder(node.left, cumsum)

            # process right subtree
            preorder(node.right, cumsum)
            
            # remove the current sum from the hashmap
            # in order not to use it during 
            # the parallel subtree processing
            freq[cumsum] -= 1
            
        count = 0
        freq = defaultdict(int)
        preorder(root, 0)

        return count