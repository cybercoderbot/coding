class MinStack(object):

    """
    Use two stacks.
    Use stack to store all vals, and use minstack to store the min val.
    When updating the stack, update the minstack as well

    For push:
    stack.append(x)
    minStack.append( min( minStack.top(), x ) )

    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            x = self.stack.pop()
        if self.minstack and x == self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
