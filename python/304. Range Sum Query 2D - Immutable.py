class NumMatrix(object):
    
    
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.matrix = []
        else:
            r,c = len(matrix), len(matrix[0])
            self.matrix = matrix
            for i in range(r):
                for j in range(1,c):
                    self.matrix[i][j] += self.matrix[i][j-1] 
                    
            for j in range(c):
                for i in range(1,r):
                    self.matrix[i][j] += self.matrix[i-1][j]
    
    def sumRegion(self, i1, j1, i2, j2):
        if not self.matrix:
            return 0
        res = self.matrix[i2][j2] 
        if i1 > 0: res -= self.matrix[i1-1][j2]
        if j1 > 0: res -= self.matrix[i2][j1-1]
        if i1 > 0 and j1 > 0: res += self.matrix[i1-1][j1-1]
        return res
        

   
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



