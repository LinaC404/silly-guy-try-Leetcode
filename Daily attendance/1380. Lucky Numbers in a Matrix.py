import numpy as np
class Solution(object):
    def myluckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        Runtime: 231 ms, faster than 12.20% of Python online submissions for Lucky Numbers in a Matrix.
        Memory Usage: 25.8 MB, less than 6.50% of Python online submissions for Lucky Numbers in a Matrix.
        """
        data = np.array(matrix)
        res = []
        for i in range(data.shape[0]):
           row_min_v = np.amin(data[i])
           row_min_i = np.where(data[i] == np.amin(data[i]))[0]
           col_max_v = np.amax(data[:, row_min_i])
           if row_min_v == col_max_v:
               res.append(row_min_v)
        return res
    def luckyNumbers (self, matrix):
        """
        Runtime: 96 ms, faster than 96.75% of Python online submissions for Lucky Numbers in a Matrix.
        Memory Usage: 13.7 MB, less than 82.11% of Python online submissions for Lucky Numbers in a Matrix.
        """
        return set(map(min, matrix)) & set(map(max, zip(*matrix)))


        
if __name__ == "__main__":
    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    a = Solution()
    a.luckyNumbers(matrix)