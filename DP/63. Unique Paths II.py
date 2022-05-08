import math
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        Runtime: 66 ms, faster than 35.39% of Python3 online submissions for Unique Paths II.
        Memory Usage: 14 MB, less than 75.75% of Python3 online submissions for Unique Paths II.
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            if obstacleGrid[0][i]==0:
                dp[0][i] = 1
            else:
                break
        for j in range(m):
            if obstacleGrid[j][0]==0:
                dp[j][0]=1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]
        
if __name__=="__main__":
    obstacleGrid = [[0,1,0],[0,1,0],[0,0,0]]
    a = Solution()
    print(a.uniquePathsWithObstacles(obstacleGrid))