class MinStack(object):

    # 解题思路：
    # 双栈法，栈stack存储当前的所有元素，minstack存储栈中的最小元素。
    # 在操作元素栈stack的同时，维护最小值栈minstack。
    
    # 对于push（x）操作：
    # stack.append( x )
    # minStack.append( min( minStack.top(), x ) )


    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack=[]
        
        
    # @return an integer
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack)==0 or x <= self.minstack[-1]:
            self.minstack.append(x)
        self.stack.append(x)
        
        
    # @return nothing
    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack)>0 and self.stack.pop()==self.minstack[-1]:
            self.minstack.pop()
            
            
    # @return an integer
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    
    # @return an integer
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




