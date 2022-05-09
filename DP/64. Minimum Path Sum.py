class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Runtime: 72 ms, faster than 93.04% of Python online submissions for Minimum Path Sum.
        Memory Usage: 13.7 MB, less than 98.68% of Python online submissions for Minimum Path Sum.
        """
        dp = [0] * len(grid[0])
        dp[0] = grid[0][0]
        for i in range(1,len(grid[0])):
            dp[i] = grid[0][i]+dp[i-1]
        for m in range(1,len(grid)):
            dp[0] += grid[m][0]
            for n in range(1,len(grid[0])):
                dp[n] = min(dp[n],dp[n-1])+grid[m][n]
        return dp[-1] 

        
if __name__=="__main__":
    a = Solution()
    print(a.minPathSum([[1,2,3],[4,5,6]]))