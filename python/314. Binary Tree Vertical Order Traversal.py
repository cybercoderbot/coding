"""
314. Binary Tree Vertical Order Traversal
Medium

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]


Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



from collections import defaultdict

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        colTable = defaultdict(list)
        queue = deque([(0, root)])

        while queue:
            col, node = queue.popleft()

            if node:
                colTable[col].append(node.val)
                queue.append((col-1, node.left))
                queue.append((col+1, node.right))
                        
        return [colTable[x] for x in sorted(colTable.keys())]


class Solution(object):
    
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        this problem seemed very hard but actually once you draw a picture on a paper or in your brain, it becomes pretty clear.
        - for the left  node, you set its index as index - 1
        - for the right node, you set its index as index + 1
        - use queue to loop through all the nodes in a tree
        - set index as a key to the hashmap() and value as a list of vals
        - add node.data into hashmap() with index as a key
        - keep track of min and max index and store into solution list and return it
        """

        if not(root): 
            return []


        MIN, MAX = 0, 0
        table = {}
        queue = [(0, root)]
        res = []

        while queue:
            # order matters
            index, node = queue.pop(0)
            if index not in table:
                table[index] = [node.val]
            else:
                table[index].append(node.val)

            # left comes first.
            if node.left:
                MIN = min(MIN, index-1)
                queue.append((index-1, node.left))
            if node.right:
                MAX = max(MAX, index+1)
                queue.append((index+1, node.right))

        for i in range(MIN, MAX+1):
            res.append(table[i])

        return res