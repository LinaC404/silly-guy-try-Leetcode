class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        Runtime: 40 ms, faster than 13.21% of Python online submissions for Integer Break.
        Memory Usage: 13 MB, less than 100.00% of Python online submissions for Integer Break.
        """
        N = n+1
        dp = [i-1 for i in range(N)]
        for i in range(2,N):
            for j in range(i+1,N):
                dp[j] = max(dp[j],max(dp[j-i],j-i)*i)
        return dp[-1]



if __name__=="__main__":
    a = Solution()
    print(a.integerBreak(n=2))