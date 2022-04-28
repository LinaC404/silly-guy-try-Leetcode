class Nummatrixrix:
    """
    Runtime: 2623 ms, faster than 29.10% of Python3 online submissions for Range Sum Query 2D - Immutable.
    Memory Usage: 25 MB, less than 54.12% of Python3 online submissions for Range Sum Query 2D - Immutable.
    """

    def __init__(self, matrix):
        self._N = len(matrix)
        self._M = len(matrix[0])
        self.presum = [[0 for i in range(self._M)] for j in range(self._N)]      
        # get the self.presum
        for i in range(self._N):
            all = 0
            for j in range(self._M):
                all += matrix[i][j]
                self.presum[i][j] = all
                if i>0:
                   self.presum[i][j] += self.presum[i-1][j]
        

    def sumRegion(self, row1, col1, row2, col2):
        ans = self.presum[row2][col2]
        if row1>0: ans -= self.presum[row1-1][col2]
        if col1>0: ans -= self.presum[row2][col1-1]
        if row1>0 and col1>0: ans += self.presum[row1-1][col1-1]
        return ans


# Your Nummatrixrix object will be instantiated and called as such:
# obj = Nummatrixrix(matrixrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)