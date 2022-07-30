"""
1650. Lowest Common Ancestor of a Binary Tree III
Medium

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Solution:
The idea is fairly simple (and the same as finding the convergence point of 2 linked lists). 
We keep two pointers, p1 and p2. Originally, these pointers point to q and p, respectively. 
Then we follow their parent pointers until they point to the same node. When either of the pointers 
points to root, we set it to the other original starting node. For example, when p1 points to root 
(i.e p1.parent is None), assign q to p1.

"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        while q:
            visited.add(q.val)
            q = q.parent

        while p:
            if p.val in visited:
                return p
            visited.add(p.val)
            p = p.parent

        return None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1 else q
            p2 = p2.parent if p2 else p

        return p1
