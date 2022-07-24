"""
1028. Recover a Tree From Preorder Traversal
Hard

We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.


Example 1:
Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:
Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:
Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]

Explanation
We save the construction path in a stack.
In each loop,
we get the number level of '-'
we get the value val of node to add.

If the size of stack is bigger than the level of node,
we pop the stack until it's not.

Finally we return the first element in the stack, as it's root of our tree.

Complexity
Time O(N), Space O(N)
"""


def recoverFromPreorder(self, s):
    stack, i = [], 0

    while i < len(s):
        level, val = 0, ""
        while i < len(s) and s[i] == '-':
            level += 1
            i += 1
        while i < len(s) and s[i] != '-':
            val += s[i]
            i += 1
        while len(stack) > level:
            stack.pop()

        node = TreeNode(val)

        if stack and not stack[-1].left:
            stack[-1].left = node
        elif stack:
            stack[-1].right = node
        stack.append(node)

    return stack[0]


class Solution:
    def recoverFromPreorder(self, s: str) -> TreeNode:
        stack = []
        depth, val = 0, ""

        for i, c in enumerate(s):
            if c == "-":
                depth += 1
                val = ""
            else:
                val += s[i]
                if i+1 == len(s) or s[i+1] == "-":
                    node = TreeNode(int(val))
                    while len(stack) > depth:
                        stack.pop()
                    if stack:
                        if not stack[-1].left:
                            stack[-1].left = node
                        else:
                            stack[-1].right = node
                    stack.append(node)
                    depth = 0
        return stack[0]
