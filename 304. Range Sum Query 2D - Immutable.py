class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.mymatrix = [[0 for i in range(self.n+1)] for j in range(self.m)]
        for i in range(self.m):
            self.mymatrix[i][1] = self.matrix[i][0]
        for i in range(0,len(self.matrix)):
            for j in range(1,len(self.matrix[0])):
                self.mymatrix[i][j+1] = self.matrix[i][j]+self.mymatrix[i][j]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for q in range(row1,row2+1):
            res = res + self.mymatrix[q][col2+1]-self.mymatrix[q][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
if __name__=="__main__":
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    obj = NumMatrix(matrix)
    param_1 = obj.sumRegion(2, 1, 4, 3)
    param_2 = obj.sumRegion(1, 1, 2, 2)
    param_3 = obj.sumRegion(1, 2, 2, 4)

