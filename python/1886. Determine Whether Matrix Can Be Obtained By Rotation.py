"""
1886. Determine Whether Matrix Can Be Obtained By Rotation
Easy

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

"""


"""
134

That's a clever bit.

First, as noted in a comment, in Python 3 zip() returns an iterator, so you need to enclose the whole thing in list() to get an actual list back out, so as of 2020 it's actually:

list(zip(*original[::-1]))
Here's the breakdown:

[::-1] - makes a shallow copy of the original list in reverse order. Could also use reversed() which would produce a reverse iterator over the list rather than actually copying the list (more memory efficient).
* - makes each sublist in the original list a separate argument to zip() (i.e., unpacks the list)
zip() - takes one item from each argument and makes a list (well, a tuple) from those, and repeats until all the sublists are exhausted. This is where the transposition actually happens.
list() converts the output of zip() to a list.
So assuming you have this:

[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]
You first get this (shallow, reversed copy):

[ [7, 8, 9],
  [4, 5, 6],
  [1, 2, 3] ]
Next each of the sublists is passed as an argument to zip:

zip([7, 8, 9], [4, 5, 6], [1, 2, 3])
zip() repeatedly consumes one item from the beginning of each of its arguments and makes a tuple from it, until there are no more items, resulting in (after it's converted to a list):

[(7, 4, 1), 
 (8, 5, 2), 
 (9, 6, 3)]
And Bob's your uncle.

To answer @IkeMiguel's question in a comment about rotating it in the other direction, it's pretty straightforward: you just need to reverse both the sequences that go into zip and the result. The first can be achieved by removing the [::-1] and the second can be achieved by throwing a reversed() around the whole thing. Since reversed() returns an iterator over the list, we will need to put list() around that to convert it. With a couple extra list() calls to convert the iterators to an actual list. So:

rotated = list(reversed(list(zip(*original))))
We can simplify that a bit by using the "Martian smiley" slice rather than reversed()... then we don't need the outer list():

rotated = list(zip(*original))[::-1]
Of course, you could also simply rotate the list clockwise three times. :-)
"""


def rotate_matrix(matrix):
    tuples = zip(*matrix[::-1])
    return [list(x) for x in tuples]
    # return map(list, tuples)


class Solution:
    def findRotation(self, matrix: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if matrix == target:
                return True
            matrix = [list(x) for x in zip(*matrix[::-1])]
        return False
