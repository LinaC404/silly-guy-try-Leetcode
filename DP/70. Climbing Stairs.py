class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        Runtime: 22 ms, faster than 55.87% of Python online submissions for Climbing Stairs.
        Memory Usage: 13.3 MB, less than 62.89% of Python online submissions for Climbing Stairs.
        """          
        if n==1: return 1
        dp = [0] * (n + 1)
        dp[1] = 1 
        dp[2] = 2 
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] 

        return dp[n]
            