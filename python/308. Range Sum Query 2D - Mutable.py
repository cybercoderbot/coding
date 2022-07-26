class NumMatrix(object):
    # Simple sum array on one dimension, O(n) for both update and sum
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix

        for row in self.matrix:
            for j in range(1, len(row)):
                row[j] += row[j-1]

    def update(self, i, j, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        original = self.matrix[i][j]

        if j > 0:
            original -= self.matrix[i][j-1]

        diff = val - original
        c = len(self.matrix[0])
        for k in range(j, c):
            self.matrix[i][k] += diff

    def sumRegion(self, i1, j1, i2, j2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        rgsum = 0
        for x in range(i1, i2+1):
            rgsum += self.matrix[x][j2]
            if j1 > 0:
                rgsum -= self.matrix[x][j1-1]
        return rgsum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
