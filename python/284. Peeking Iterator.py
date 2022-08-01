"""
284. Peeking Iterator
Medium

Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.

Implement the PeekingIterator class:

PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
int next() Returns the next element in the array and moves the pointer to the next element.
boolean hasNext() Returns true if there are still elements in the array.
int peek() Returns the next element in the array without moving the pointer.
Note: Each language may have a different implementation of the constructor and Iterator, but they all support the int next() and boolean hasNext() functions.

Example 1:
Input
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 2, 2, 3, false]
"""


class PeekingIterator:
    """
    Define a buffer which stores the next value to be used by the iterator class.
    """

    def __init__(self, iterator):
        self.iter = iterator
        self.buff = None

    def peek(self):
        if not self.buff:
            self.buff = self.iter.next()
        return self.buff

    def next(self):
        if not self.buff:
            return self.iter.next()
        res = self.buff
        self.buff = None
        return res

    def hasNext(self):
        return not self.buff or self.iter.hasNext()
