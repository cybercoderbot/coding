class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s)%2!=0: return False
        
        opening = set('([{')
        closing = set(')]}')
        
        d = {'(': ')', '[': ']', '{': '}'}
        stack = []
        
        for c in s:
            if c in opening:
                stack.append(c)
            elif c in closing:
                if not stack: 
                    return False
                if stack and c != d[stack.pop()]:
                    return False
        if stack:
            return False
        
        return True
                
                
                
                
                
                
