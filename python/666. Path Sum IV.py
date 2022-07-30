"""
666. Path Sum IV
Medium

If the depth of a tree is smaller than 5, then this tree can be represented by an array of three-digit integers. For each integer in this array:

The hundreds digit represents the depth d of this node where 1 <= d <= 4.
The tens digit represents the position p of this node in the level it belongs to where 1 <= p <= 8. The position is the same as that in a full binary tree.
The units digit represents the value v of this node where 0 <= v <= 9.
Given an array of ascending three-digit integers nums representing a binary tree with a depth smaller than 5, return the sum of all paths from the root towards the leaves.

It is guaranteed that the given array represents a valid connected binary tree.

Example 1:
Input: nums = [113,215,221]
Output: 12
Explanation: The tree that the list represents is shown.
The path sum is (3 + 5) + (3 + 1) = 12.

Example 2:
Input: nums = [113,221]
Output: 4
Explanation: The tree that the list represents is shown. 
The path sum is (3 + 1) = 4.
"""


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = {}
        for n in nums:
            depth, pos, val = (int(x) for x in str(n))
            tree[depth, pos] = val

        res = 0
        stack = [(1, 1, 0)]
        while stack:
            depth, pos, path = stack.pop()
            path += tree[depth, pos]
            depth += 1
            left, right = 2*pos-1, 2*pos
            if (depth, left) not in tree and (depth, right) not in tree:
                res += path
            if (depth, left) in tree:
                stack.append((depth, left, path))
            if (depth, right) in tree:
                stack.append((depth, right, path))
        return res
