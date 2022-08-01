"""
281. Zigzag Iterator
Medium

Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

Implement the ZigzagIterator class:

ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
boolean hasNext() returns true if the iterator still has elements, and false otherwise.
int next() returns the current element of the iterator and moves the iterator to the next element.

Example 1:
Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
"""


class ZigzagIterator:
    """
    Time: O(N), Space: O(N)
    """

    def __init__(self, v1: List[int], v2: List[int]):
        self.vals = []
        if v1:
            self.vals.append(v1)
        if v2:
            self.vals.append(v2)

    def next(self) -> int:
        vec = self.vals.pop(0)
        res = vec.pop(0)
        if vec:
            self.vals.append(vec)
        return res

    def hasNext(self) -> bool:
        return self.vals
