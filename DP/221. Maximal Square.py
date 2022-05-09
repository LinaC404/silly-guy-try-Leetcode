import math
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        Runtime: 543 ms, faster than 56.22% of Python online submissions for Maximal Square.
        Memory Usage: 34.9 MB, less than 19.07% of Python online submissions for Maximal Square.
        """
        dp = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        ans = 1 if sum(map(sum,dp))>0 else 0
        if ans == 0: return 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                cell = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                if dp[i][j] == 0 or cell == 0:
                    pass
                else:
                    dp[i][j] = int(math.sqrt(cell)+1)**2    
                ans = max(dp[i][j],ans)
        return ans


if __name__=="__main__":
    a = Solution()
    print(a.maximalSquare([["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]))